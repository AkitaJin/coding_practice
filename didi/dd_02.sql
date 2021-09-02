-- dd_02
-- oid
-- amount
-- bu
-- ch
select * from pivot (sum(amount) for bu in ('快车','顺风车','出租车','巴士','小巴'))