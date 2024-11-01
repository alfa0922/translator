-- Create table
CREATE TABLE app.hist_msg_port
(
  idmsg           NUMBER,
  text            CLOB,
  data_mgs        DATE         DEFAULT SYSDATE,
  usuario         VARCHAR2(30) DEFAULT USER,
  flg_lang        INTEGER
)
tablespace USERS
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  )
nologging;