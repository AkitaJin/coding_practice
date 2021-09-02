-- table dd
-- pid 人ID
-- oid 订单ID
-- time 年月日时分秒
-- 每个人每天最后一笔
select *
from
(select
pid, oid, time,row_number() as ranking over (partition by pid,DAY(time) order by time desc)
from dd)
where ranking=1