Top1-AutomatedFrameworkPython3and2-in2019-Robot

See http://robotframework.org

To run a RobotFramework TC 
(1) python sut/login.py create fred P4ssw0rd	(Actual Result: SUCCESS)

(2) Negative TestScenario_a:
python sut/login.py login nobody P4ssw0rd
Expected Result: Access Denied
Actual Result: As expected	(Actual Result Quoted: Access Denied)

(3) python sut/login.py login fred P4ssw0rd	(Actual Result: Logged In)

(4) python sut/login.py create david short	(Note: NegativeTestScenario_b)	(Actual Result: Creating user failed: Password must be 7-12 characters long)

(5) python sut/login.py create dave invalid	(Note: NegativeTestScenario_c)	(Actual Result: Creating user failed: Password must be a combination of lowercase and uppercase letters and numbers)

(6) python sut/login.py change-password fred wrong NewP4ss	(Note: NegativeTestScenario_d)	(Actual Result: Changing password failed: Access Denied)

(7) python sut/login.py change-password fred P4ssw0rd short	(Note: NegativeTestScenario_e)	(Actual Result: Changing password failed: Password must be 7-12 characters long)

(8) [Skip] python sut/login.py change-password fred P4ssw0rd NewP4ss	(Actual Result: )

(9) python sut/login.py change-password fred P4ssw0rd P4ssw0rd	(Actual Result: SUCCESS)[Note: This might be something we can expand as new feature(s)]
