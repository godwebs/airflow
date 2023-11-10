from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", #덱 이름(파이썬 파일명과 일치시키는 것이 직관적으로 좋음)
    schedule="0 0 * * *", #주기(순서대로 분,시,일,월,요일)
    start_date=pendulum.datetime(2021, 3, 1, tz="Asia/Seoul"), #언제부터 돌건지
    catchup=False, #현재 2/1이고 start_date가 1/1일 때, catchup이 true면 누락된 1월분 전부 돔(일별로 순서대로 돌지않고 1달분을 한꺼번에)
    #dagrun_timeout=datetime.timedelta(minutes=60), #60분 이상 돌면 실패
    #tags=["example", "example2"],
    #params={"example_key": "example_value"}, #태스크에 공통적으로 넘겨줄 파라미터
) as dag:
    

    bash_t1 = BashOperator(
        task_id="bash_t1", #객체명과 동일하게 주는 것이 좋음
        bash_command="echo whoami",
    )


    bash_t2 = BashOperator(
        task_id="bash_t2", #객체명과 동일하게 주는 것이 좋음
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2 #태스크 순서