CREATE DATABASE IF NOT EXISTS cmcd;
USE cmcd;

CREATE TABLE cmcd.cmcd_data
(
    time datetime     null,
    br   int          null,
    bl   int          null,
    bs   tinyint(1)   null,
    cid  varchar(64) null,
    d    int          null,
    dl   int          null,
    mtp  int          null,
    nor  varchar(255) null,
    nrr  varchar(255) null,
    ot   char(2)      null,
    pr   DECIMAL(4,2) null,
    rtp  int          null,
    sf   char         null,
    sid  varchar(64)  null,
    st   char         null,
    su   tinyint(1)   null,
    tb   int          null
);


CREATE USER 'node'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON cmcd.* TO 'node'@'%';
