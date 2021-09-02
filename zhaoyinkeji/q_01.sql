-- 客户表
UDM.CLT(
CLT_NBR CHAR(6) PRIMARY KEY,  --客户编号
CLT_NAM VARCHAR(100),   --客户名称
CLT_STS CHAR(1),   --客户状态 0正常，1注销
CLT_TYP CHAR(1)  --零售1，对公2
)
-- 数据量100万

-- 帐户表
UDM.ACT(
ACT_NBR VARCHAR(20) PRIMARY KEY, --帐户编号***
CLT_NBR CHAR(6)  --客户编号
)
-- 数据量700万

-- 交易表
UDM.TRX(
  SEQ_NBR VARCHAR(30) PRIMARY KEY,  --交易序列号
TRX_DTE DATE,  --交易日期****
ACT_NBR VARCHAR(20),  --帐户编号
CCY_NBR CHAR(2),  --币种 10的时候，AMT为空
TRX_AMT  DECIMAL(19,2),  --金额
RMB_AMT DECIMAL(19,2)  --折人民币金额
) 
-- 数据量10亿

其中TRX_DTE和ACT_NBR是索引，当CCY_NBR='10'时，RMB_AMT为空
请编写SQL提取2021年5月份的交易额10大的对公客户信息，包含客户名称，交易额，交易笔数
select 

from
UDM.CLT a join UDM.ACT b on a.CLT_NBR=b.CLT_NBR
join

select sum(RMB_AMT case when )