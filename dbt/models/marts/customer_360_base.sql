select c.customer_id,c.customer_name,c.city,c.state,c.plan,c.status as customer_status,
coalesce(r.total_recharge,0) as total_recharge,coalesce(r.recharge_count,0) as recharge_count,
coalesce(u.total_data_gb,0) as total_data_gb,coalesce(u.total_call_minutes,0) as total_call_minutes,
coalesce(u.total_sms,0) as total_sms,coalesce(x.complaint_count,0) as complaint_count,
coalesce(x.avg_resolution_days,0) as avg_resolution_days
from {{ source('bronze','customers') }} c
left join (select customer_id,sum(amount) total_recharge,count(*) recharge_count from {{ source('bronze','recharge') }} group by customer_id) r using(customer_id)
left join (select customer_id,sum(data_used_gb) total_data_gb,sum(call_minutes) total_call_minutes,sum(sms_count) total_sms from {{ source('bronze','usage') }} group by customer_id) u using(customer_id)
left join (select customer_id,count(*) complaint_count,avg(resolution_days) avg_resolution_days from {{ source('bronze','complaints') }} group by customer_id) x using(customer_id)
