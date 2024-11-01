CREATE OR REPLACE TRIGGER app.TRG_INS_HIST_MSG_PORT

BEFORE INSERT
ON app.hist_msg_port

REFERENCING NEW AS NEW OLD AS OLD

FOR EACH ROW

 DECLARE

     vidmsg         app.hist_msg_port.idmsg%TYPE := NULL;

 BEGIN

   SELECT MAX(t.idmsg) + 1
   INTO   vidmsg
   FROM   app.hist_msg_port t;

   IF vidmsg IS NULL THEN

      :NEW.idmsg := 1;

   ELSE
      :NEW.idmsg := vidmsg;


   END IF;


 END;