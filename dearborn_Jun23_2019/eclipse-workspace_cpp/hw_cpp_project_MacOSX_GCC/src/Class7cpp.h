#include <string>
#ifndef CLASS7CPP_H_
#define CLASS7CPP_H_

namespace std {
class Class7_cpp {
private:
	string courseName;
public:
	Class7_cpp(string);
	void setCourseName(string);
	string getCourseName();
	void displayMessage();
	virtual ~Class7_cpp();
};
}
#endif
