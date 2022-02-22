#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

using namespace std;

string file_name = "/home/joaovitor/Documents/ForPaper/data/662_bus.mtx";

int main(int argc, char *argv[])
{

    int od1, od2, NE, NV;

    vector<pair<int,int>> OD;

	ifstream f_inst(file_name);

	if (!f_inst.is_open())
	{
		cout << "ERROR: File " << file_name << " not found!" << endl;
		exit(0);
	}

	f_inst>>NV;
	f_inst>>NE;

	for(int i=0; i<NE; ++i){
		
    	f_inst>> od1;
		f_inst>> od2;
		if(od1!=od2){
			OD.emplace_back(make_pair(od1,od2));
		}
	}
	cout<<NV<<" "<<NE<<endl;

    for (int i=0; i<OD.size();++i){
        cout<<OD[i].first<<" ";
        cout<<OD[i].second<<endl;
    }

return 0;

}
