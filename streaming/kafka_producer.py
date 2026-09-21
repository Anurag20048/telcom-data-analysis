import json,os,random,time
from datetime import datetime,timezone
from kafka import KafkaProducer
producer=KafkaProducer(bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092"),value_serializer=lambda v:json.dumps(v).encode(),acks="all",retries=5)
topic=os.getenv("KAFKA_TOPIC","telecom-events")
for i in range(100):
    event={"event_id":f"evt-{int(time.time())}-{i}","event_type":random.choice(["usage","network","recharge","complaint"]),"customer_id":random.randint(100001,101000),"event_time":datetime.now(timezone.utc).isoformat(),"source":"telecom-simulator"}
    producer.send(topic,event); print("sent:",event["event_id"]); time.sleep(.5)
producer.flush()
