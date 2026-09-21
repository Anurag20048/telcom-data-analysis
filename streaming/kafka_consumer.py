import json,os
from kafka import KafkaConsumer
consumer=KafkaConsumer(os.getenv("KAFKA_TOPIC","telecom-events"),bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092"),group_id="telecom-pipeline",auto_offset_reset="earliest",value_deserializer=lambda v:json.loads(v.decode()))
seen=set()
for message in consumer:
    event=message.value; event_id=event["event_id"]
    if event_id in seen: continue
    seen.add(event_id)
    print(f"processed event={event_id} type={event['event_type']} customer={event['customer_id']}")
