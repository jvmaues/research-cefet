#include <string>
#include <fstream>
#include <vector>
#include <utility> // std::pair

using namespace std;

typedef std::pair< std::string, int> Pair;

void write_csv(std::string filename, std::vector<string> columns, std::vector<string>names,  std::vector<int>init_band, std::vector<int> band){
    // Create an output filestream object
    std::ofstream myFile(filename);

     // Send column names to the stream
    for(int j = 0; j < columns.size(); ++j)
    {
        myFile << columns.at(j);

        if(j != columns.size()-1) myFile << ","; // No comma at end of line
    };

    myFile << "\n";

    // Send data to the stream
    for(int i = 0; i < names.size(); ++i){
        
        myFile << names.at(i);
        myFile << ",";
        myFile << init_band.at(i);
        myFile << ",";
        myFile << band.at(i);

        myFile << "\n";
    }

    myFile.close();

};

int main() {
    // Make three vectors, each of length 100 filled with 1s, 2s, and 3s

    std::vector<string> colums = {"Instance_name", "initial_bandwitch", "bandwitch"};
    std::vector<string> instances = {"name01", "name02", "name03"};
    std::vector<int> initial_bandwitch = {20, 30, 40};
    std::vector<int> final_bandwitch = {10, 20, 30};

    write_csv("three_cols.csv", colums, instances, initial_bandwitch, final_bandwitch);
    
    return 0;
}