# Schema Audit Report: `xdt_mlf`

**Total Tables:** 19

---

### 1. ccg_log_storesorder
- **Rows:** 0
- **Columns (39):** `logid`, `logtime`, `logdesc`, `loguser`, `logmemo`, `orderid`, `orderstate`, `plantid`, `bookdate`, `weekno`, `booktimeseqno`, `booktimestart`, `booktimeend`, `userid`, `custname`, `custmobile`, `carmodelid`, `platenumber`, `active`, `sysdate`, `sysuserid`, `sysusername`, `upddate`, `upduserid`, `updusername`, `confirmfrom`, `confirmdate`, `confirmuserid`, `confirmusername`, `cancelfrom`, `canceldate`, `canceluserid`, `cancelusername`, `closefrom`, `closedate`, `closeuserid`, `closeusername`, `ftp_date`, `custmobile_09`

### 2. ccg_v_storesorder
- **Rows:** 0
- **Columns (67):** `orderid`, `orderstate`, `orderstatedesc`, `userid`, `accountnumber`, `custname`, `userlv`, `userlvname`, `custmobile`, `weekno`, `weeknodesc`, `booktype`, `booktypedesc`, `bookdate`, `strbookdate`, `booktimestart`, `booktimeend`, `strbooktimestart`, `strbooktimeend`, `booktimedesc`, `booktimeseqno`, `actid`, `actname`, `plantid`, `plantname`, `seoname`, `contactphone`, `contactmobile`, `mgrname`, `cityid`, `cityname`, `areaid`, `areaname`, `platenumber`, `brandid`, `brandnameen`, `brandnamech`, `carbranddesc`, `seriesid`, `seriesname`, `carmodelid`, `modelname`, `carmodeldesc`, `sysdate`, `strsysdate`, `shortsysdate`, `shortsystime`, `sysuserid`, `sysusername`, `upddate`, `strupddate`, `upduserid`, `updusername`, `logmemo`, `confirmfrom`, `confirmdate`, `strconfirmdate`, `confirmuserid`, `confirmusername`, `cancelfrom`, `canceldate`, `strcanceldate`, `canceluserid`, `cancelusername`, `ftp_date`, `custmobile_09`, `contactmobile_09`

### 3. ccg_v_usercar
- **Rows:** 0
- **Columns (21):** `carid`, `platenumber`, `userid`, `username`, `binded`, `binddate`, `brandid`, `brandnameen`, `brandnamech`, `carbranddesc`, `seriesid`, `seriesname`, `modelid`, `modelname`, `carmodeldesc`, `active`, `sysdate`, `sysuser`, `upddate`, `upduser`, `ftp_date`

### 4. ccg_v_users
- **Rows:** 0
- **Columns (36):** `userid`, `accountnumber`, `username`, `userlv`, `userlvname`, `passwordhash`, `gender`, `gendername`, `birthday`, `strbirthday`, `userphotofileid`, `pictureurl`, `email`, `emailconfirmed`, `emailcheckdesc`, `emailcheck`, `phonenumber`, `phonenumberconfirmed`, `phonecheckdesc`, `phonecheck`, `changepw`, `active`, `stractive`, `activedesc`, `sysdate`, `strsysdate`, `shortsysdate`, `shortsystime`, `upddate`, `strupddate`, `upduser`, `roadtransferremark`, `roadissuedate`, `roadvaliddate`, `ftp_date`, `phonenumber_09`

### 5. dms_jobticket
- **Rows:** 0
- **Columns (44):** `column_1`, `column_2`, `column_3`, `column_4`, `column_5`, `column_6`, `column_7`, `column_8`, `column_9`, `column_10`, `column_11`, `column_12`, `column_13`, `column_14`, `column_15`, `column_16`, `column_17`, `column_18`, `column_19`, `column_20`, `column_21`, `column_22`, `column_23`, `column_24`, `column_25`, `column_26`, `column_27`, `column_28`, `column_29`, `column_30`, `column_31`, `column_32`, `column_33`, `column_34`, `column_35`, `column_36`, `column_37`, `column_38`, `column_39`, `column_40`, `column_41`, `column_42`, `exportbigquerydate`, `ftp_date`

### 6. mlf_caas_v_car
- **Rows:** 0
- **Columns (24):** `carid`, `memberid`, `membername`, `mobilephone`, `mobilephone_09`, `vmscarid`, `allianceno`, `sourcefrom`, `platenumber`, `vinnumber`, `brandid`, `brandname`, `seriesid`, `seriesname`, `modelid`, `modelname`, `licensedate`, `orgissueddate`, `notes`, `applicationstatus`, `applicationdate`, `ftp_date`, `_etl_time`, `upddate`

### 7. mlf_caas_v_member
- **Rows:** 0
- **Columns (41):** `memberid`, `membername`, `nickname`, `userkind`, `userkinddesc`, `accountnumber`, `passwordhash`, `changepw`, `gender`, `genderdesc`, `mobilephone`, `mobilephoneconfirmed`, `email`, `emailconfirmed`, `phonenumberhome`, `phonenumberoffice`, `birthday`, `birthdaymonth`, `addrcityid`, `addrareaid`, `addrroad`, `notes`, `active`, `sourcefrom`, `sourceallianceno`, `sourcealliancename`, `providerbinded`, `sysuserid`, `sysusername`, `sysdate`, `upduserid`, `updusername`, `upddate`, `registersource`, `registersourceid`, `registertype`, `registertypeid`, `notificationtype`, `ftp_date`, `_etl_time`, `mobilephone_09`

### 8. mlf_vms_log_jobticketdetail
- **Rows:** 0
- **Columns (37):** `logid`, `logtime`, `logdesc`, `loguser`, `logmemo`, `seqno`, `jobticketid`, `agformnr`, `vehiclemaintenanceplantid`, `accounttype`, `jobtype`, `jobitemno`, `jobitemid`, `pjobitemid`, `itemtype`, `itemdesc`, `descname`, `pricetype`, `listprice`, `listpricecanedit`, `discount`, `discountcanedit`, `saleprice`, `quantity`, `quantitycanedit`, `techid`, `techname`, `benexttime`, `active`, `sysuserid`, `sysusername`, `sysdate`, `upduserid`, `updusername`, `upddate`, `ftp_date`, `_etl_time`

### 9. mlf_vms_log_jobticketmain
- **Rows:** 854700
- **Columns (29):** `logid`, `logtime`, `logdesc`, `loguser`, `logmemo`, `jobticketid`, `carid`, `agformnr`, `vehiclemaintenanceplantid`, `vehiclemaintenanceplantname`, `memid`, `platenumber`, `vinnumber`, `jobtickettype`, `currentkm`, `inplantdate`, `deliverydate`, `accountdate`, `jobticketstatus`, `notes`, `active`, `sysuserid`, `sysusername`, `sysdate`, `upduserid`, `updusername`, `upddate`, `ftp_date`, `_etl_time`

### 10. mlf_vms_v_jobticket
- **Rows:** 181796
- **Columns (44):** `jobticketid`, `carid`, `agformnr`, `memid`, `memname`, `memnameabbr`, `platenumber`, `vinnumber`, `vehiclemaintenanceplantid`, `vehiclemaintenanceplantname`, `alliancename`, `dealername`, `fulladdrroad`, `contactphone`, `contactmobile`, `taxid`, `fax`, `jobtickettype`, `jobtickettypedesc`, `jobticketwage`, `currentkm`, `inplantdate`, `inplantdatestr`, `deliverydate`, `deliverydatestr`, `accountdate`, `accountdatestr`, `jobticketstatus`, `jobticketstatusdesc`, `salaryamount`, `partamount`, `totalamount`, `notes`, `active`, `sysuserid`, `sysusername`, `sysdate`, `sysdatestr`, `upduserid`, `updusername`, `upddate`, `ftp_date`, `contactmobile_09`, `_etl_time`

### 11. mlf_vms_v_jobticketdetail
- **Rows:** 9100206
- **Columns (41):** `seqno`, `jobticketid`, `agformnr`, `vehiclemaintenanceplantid`, `plantname`, `jobticketstatus`, `jobticketstatusdesc`, `accounttype`, `accounttypedesc`, `jobtype`, `jobtypedesc`, `itemtype`, `itemtypedesc`, `jobitemid`, `jobitemno`, `pjobitemid`, `pjobitemname`, `itemdesc`, `descname`, `pricetype`, `listprice`, `listpricecanedit`, `discount`, `discountcanedit`, `saleprice`, `quantity`, `quantitycanedit`, `subtotal`, `techid`, `techname`, `benexttime`, `active`, `mainactive`, `sysuserid`, `sysusername`, `sysdate`, `upduserid`, `updusername`, `upddate`, `ftp_date`, `_etl_time`

### 12. mlf_vms_v_jobticketdetail_raw
- **Rows:** 0
- **Columns (41):** `seqno`, `jobticketid`, `agformnr`, `vehiclemaintenanceplantid`, `plantname`, `jobticketstatus`, `jobticketstatusdesc`, `accounttype`, `accounttypedesc`, `jobtype`, `jobtypedesc`, `itemtype`, `itemtypedesc`, `jobitemid`, `jobitemno`, `pjobitemid`, `pjobitemname`, `itemdesc`, `descname`, `pricetype`, `listprice`, `listpricecanedit`, `discount`, `discountcanedit`, `saleprice`, `quantity`, `quantitycanedit`, `subtotal`, `techid`, `techname`, `benexttime`, `active`, `mainactive`, `sysuserid`, `sysusername`, `sysdate`, `upduserid`, `updusername`, `upddate`, `ftp_date`, `_etl_time`

### 13. mlf_vms_v_jobticket_raw
- **Rows:** 0
- **Columns (44):** `jobticketid`, `carid`, `agformnr`, `memid`, `memname`, `memnameabbr`, `platenumber`, `vinnumber`, `vehiclemaintenanceplantid`, `vehiclemaintenanceplantname`, `alliancename`, `dealername`, `fulladdrroad`, `contactphone`, `contactmobile`, `taxid`, `fax`, `jobtickettype`, `jobtickettypedesc`, `jobticketwage`, `currentkm`, `inplantdate`, `inplantdatestr`, `deliverydate`, `deliverydatestr`, `accountdate`, `accountdatestr`, `jobticketstatus`, `jobticketstatusdesc`, `salaryamount`, `partamount`, `totalamount`, `notes`, `active`, `sysuserid`, `sysusername`, `sysdate`, `sysdatestr`, `upduserid`, `updusername`, `upddate`, `ftp_date`, `contactmobile_09`, `_etl_time`

### 14. mlf_vms_v_member
- **Rows:** 0
- **Columns (34):** `memid`, `memname`, `memnameabbr`, `gender`, `genderdesc`, `memphonenumberhome`, `memphonenumberhomearea`, `memphonenumberhometel`, `memphonenumberoffice`, `memphonenumberofficearea`, `memphonenumberofficetel`, `memmobilephone`, `birthdaystr`, `birthday`, `email`, `emailconfirmed`, `idnumber`, `taxidnumber`, `addrcityid`, `addrcityname`, `addrareaid`, `addrareaname`, `addrroad`, `notes`, `memactive`, `memsysuserid`, `memsysusername`, `memsysdate`, `memupduserid`, `memupdusername`, `memupddate`, `ftp_date`, `memmobilephone_09`, `_etl_time`

### 15. mlf_vms_v_membercar
- **Rows:** 0
- **Columns (64):** `memid`, `carid`, `allianceno`, `alliancename`, `platenumber`, `platenumber1`, `platenumber2`, `warrantynumber`, `warrantydate`, `vinnumber`, `carcolor`, `carcolordesc`, `enginenumber`, `displacement`, `transmission`, `transmissiondesc`, `fueloilid`, `fueloildesc`, `brandid`, `brandname`, `seriesid`, `seriesname`, `modelid`, `modelname`, `yearofmanufactureyearstr`, `yearofmanufacturemonthstr`, `yearofmanufacture`, `drivername`, `driverphonenumber`, `licensedate`, `licensedatestr`, `orgissueddate`, `orgissueddatestr`, `carnotes`, `introducer`, `dealerid`, `dealername`, `beelectronicagreement`, `electronicagreementsysdate`, `electronicagreementsysdatestr`, `bepaperagreement`, `paperagreementsysdate`, `paperagreementsysdatestr`, `carleveldesc`, `lastjobticketdate`, `lastjobticketdatestr`, `lastkm`, `notcompletedcount`, `iswarrantyticket`, `memactive`, `memsysdate`, `memupddate`, `memupduser`, `memupdusername`, `memupduserfullname`, `caractive`, `carsysdate`, `carupddate`, `carupduser`, `carupdusername`, `carupduserfullname`, `ftp_date`, `_etl_time`, `_etl_allianceno`

### 16. mlf_vms_v_membercar_raw
- **Rows:** 658134
- **Columns (63):** `memid`, `carid`, `allianceno`, `alliancename`, `platenumber`, `platenumber1`, `platenumber2`, `warrantynumber`, `warrantydate`, `vinnumber`, `carcolor`, `carcolordesc`, `enginenumber`, `displacement`, `transmission`, `transmissiondesc`, `fueloilid`, `fueloildesc`, `brandid`, `brandname`, `seriesid`, `seriesname`, `modelid`, `modelname`, `yearofmanufactureyearstr`, `yearofmanufacturemonthstr`, `yearofmanufacture`, `drivername`, `driverphonenumber`, `licensedate`, `licensedatestr`, `orgissueddate`, `orgissueddatestr`, `carnotes`, `introducer`, `dealerid`, `dealername`, `beelectronicagreement`, `electronicagreementsysdate`, `electronicagreementsysdatestr`, `bepaperagreement`, `paperagreementsysdate`, `paperagreementsysdatestr`, `carleveldesc`, `lastjobticketdate`, `lastjobticketdatestr`, `lastkm`, `notcompletedcount`, `iswarrantyticket`, `memactive`, `memsysdate`, `memupddate`, `memupduser`, `memupdusername`, `memupduserfullname`, `caractive`, `carsysdate`, `carupddate`, `carupduser`, `carupdusername`, `carupduserfullname`, `ftp_date`, `_etl_time`

### 17. mlf_vms_v_member_raw
- **Rows:** 0
- **Columns (34):** `memid`, `memname`, `memnameabbr`, `gender`, `genderdesc`, `memphonenumberhome`, `memphonenumberhomearea`, `memphonenumberhometel`, `memphonenumberoffice`, `memphonenumberofficearea`, `memphonenumberofficetel`, `memmobilephone`, `birthdaystr`, `birthday`, `email`, `emailconfirmed`, `idnumber`, `taxidnumber`, `addrcityid`, `addrcityname`, `addrareaid`, `addrareaname`, `addrroad`, `notes`, `memactive`, `memsysuserid`, `memsysusername`, `memsysdate`, `memupduserid`, `memupdusername`, `memupddate`, `ftp_date`, `memmobilephone_09`, `_etl_time`

### 18. mlf_xms_v_notificationlist
- **Rows:** 0
- **Columns (21):** `notificationid`, `notificationtype`, `notificationtypedesc`, `sourcetype`, `sourceid`, `plantno`, `customername`, `platenumber`, `customerphone`, `customerphone_09`, `customeruid`, `notificationchannel`, `notificationcontent`, `notificationstatus`, `notificationstatusdesc`, `confirmuser`, `confirmtime`, `actualsenttime`, `ftp_date`, `_etl_time`, `upddate`

### 19. mlf_xms_v_reservation
- **Rows:** 0
- **Columns (43):** `reservationid`, `reservationstate`, `reservationstatedesc`, `sourcefrom`, `reservationfromdesc`, `servicetypeno`, `servicetypedesc`, `memberid`, `customername`, `customermobile`, `plantno`, `plantname`, `allianceno`, `bookdate`, `booktime`, `carid`, `vmscarid`, `platenumber`, `simpleplatenumber`, `brandid`, `brandname`, `jobticketid`, `agformnr`, `vehiclemaintenanceplantid`, `active`, `sysdate`, `sysuserid`, `sysusername`, `upddate`, `upduserid`, `updusername`, `confirmdate`, `confirmuserid`, `confirmusername`, `canceldate`, `canceluserid`, `cancelusername`, `closedate`, `closeuserid`, `closeusername`, `ftp_date`, `_etl_time`, `customermobile_09`

