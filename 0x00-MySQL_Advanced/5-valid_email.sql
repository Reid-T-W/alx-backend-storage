-- Trigger executed upon inserting into
-- the orders table
DROP TRIGGER IF EXISTS reset_valid_email;
CREATE TRIGGER reset_valid_email BEFORE UPDATE on users
FOR EACH ROW
SET NEW.email = NEW.email, NEW.valid_email = 
CASE
	WHEN OLD.email != NEW.email THEN 0
	ELSE 1
END
