#include <iostream>
using namespace std;

class Account {
private:
    int account_no;
    double account_bal;
    int security_code;

public:
    void initialize(int acc_no, double acc_bal, int sec_code) {
        account_no = acc_no;
        account_bal = acc_bal;
        security_code = sec_code;
    }

    void display() {
        cout << "Account No: " << account_no << endl;
        cout << "Account Balance: $" << account_bal << endl;
        cout << "Security Code: " << security_code << endl;
    }
};

int main() {
    Account myAccount;
    myAccount.initialize(12345, 2500.75, 9876);
    myAccount.display();

    return 0;
}
