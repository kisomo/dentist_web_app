#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;
/*
using std::cout; using std::cin;
using std::endl; using std::string;
using std::vector; using std::istringstream;
using std::stringstream;
*/
int main(int argc, char *argv[])
{
   /*
   fstream newfile1, newfile2; 
   newfile1.open("address_test.txt",ios::in); // read
   if (newfile1.is_open()) 
   {
      string tp;
      while(getline(newfile1, tp)) 
        { //cout << tp << "\n"; 
            newfile2.open("address_test_out.txt",ios::out); // write
            if(newfile2.is_open()) 
            { newfile2<< tp << endl;newfile2<< " " << endl; }
        } 
      newfile2.close(); 
      newfile1.close(); 
   }
   cout << "copied text from one file to the second:"<< endl;
   */
   string line; // For writing text file
    // Creating ofstream & ifstream class object
    ifstream ini_file{"address_test.txt"}; // This is the original file
    ofstream out_file{ "address_test_out.txt"};
    if (ini_file && out_file) 
    {
        while (getline(ini_file, line)) { out_file << line << "\n";}
        cout << "Hi your Copy Finished" << argv[1] << endl;
    }
    else {
        // Something went wrong
        //printf("Cannot read File");
        cout << "Cannot read File \n";
        }
    // Closing file
    ini_file.close();
    out_file.close();

   return 0;
}

