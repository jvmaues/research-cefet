//=======================================================================
// Copyright 1997, 1998, 1999, 2000 University of Notre Dame.
// Authors: Andrew Lumsdaine, Lie-Quan Lee, Jeremy G. Siek
//          Doug Gregor, D. Kevin McGrath
//
// Distributed under the Boost Software License, Version 1.0.
// (See accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)
//=======================================================================
#include <string>
#include <boost/config.hpp>
#include <vector>
#include <iostream>
#include <fstream>
#include <utility>

#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/cuthill_mckee_ordering.hpp>
#include <boost/graph/properties.hpp>
#include <boost/graph/bandwidth.hpp>

using namespace std;

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

int main(int, char*[])
{
    using namespace boost;
    using namespace std;

    typedef adjacency_list< vecS, vecS, undirectedS, property< vertex_color_t, default_color_type, property< vertex_degree_t, int > > > Graph;
    typedef graph_traits< Graph >::vertex_descriptor Vertex;
    typedef graph_traits< Graph >::vertices_size_type size_type;
    typedef std::pair< std::size_t, std::size_t > Pair;

    std::vector<string> columns = {"Instance_name", "initial_bandwitch", "bandwitch"};
    std::vector<string> instances;
    std::vector<int> original_bandwitch;
    std::vector<int> final_bandwitch;

    vector<string> filenames_list  = {"/home/joaovitor/Documents/ForPaper/data/dwt_918.mtx", "/home/joaovitor/Documents/ForPaper/data/bcspwr04.mtx", "/home/joaovitor/Documents/ForPaper/data/can_445.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/gre__512.mtx", "/home/joaovitor/Documents/ForPaper/data/gr_30_30.mtx", "/home/joaovitor/Documents/ForPaper/data/bcsstm07.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/impcol_a.mtx", "/home/joaovitor/Documents/ForPaper/data/bcsstk06.mtx", "/home/joaovitor/Documents/ForPaper/data/fs_760_1.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/dwt_592.mtx", "/home/joaovitor/Documents/ForPaper/data/hor__131.mtx", "/home/joaovitor/Documents/ForPaper/data/ash292.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/gre__343.mtx", "/home/joaovitor/Documents/ForPaper/data/can_292.mtx", "/home/joaovitor/Documents/ForPaper/data/can_838.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/dwt_221.mtx", "/home/joaovitor/Documents/ForPaper/data/bcsstk20.mtx", "/home/joaovitor/Documents/ForPaper/data/dwt_310.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/bcsstk19.mtx", "/home/joaovitor/Documents/ForPaper/data/dwt_878.mtx", "/home/joaovitor/Documents/ForPaper/data/dwt_419.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/impcol_e.mtx", "/home/joaovitor/Documents/ForPaper/data/dwt_209.mtx", "/home/joaovitor/Documents/ForPaper/data/bp_0.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/bp_800.mtx", "/home/joaovitor/Documents/ForPaper/data/bp_1000.mtx", "/home/joaovitor/Documents/ForPaper/data/685_bus.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/494_bus.mtx", "/home/joaovitor/Documents/ForPaper/data/bp_1400.mtx", "/home/joaovitor/Documents/ForPaper/data/bcspwr05.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/bp_1200.mtx", "/home/joaovitor/Documents/ForPaper/data/bp_400.mtx", "/home/joaovitor/Documents/ForPaper/data/dwt_245.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/impcol_d.mtx", "/home/joaovitor/Documents/ForPaper/data/662_bus.mtx", "/home/joaovitor/Documents/ForPaper/data/bp_600.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/gre_216a.mtx", "/home/joaovitor/Documents/ForPaper/data/can_715.mtx", "/home/joaovitor/Documents/ForPaper/data/dwt_992.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/bp_1600.mtx", "/home/joaovitor/Documents/ForPaper/data/fs_680_1.mtx", "/home/joaovitor/Documents/ForPaper/data/dwt_361.mtx",
                                    "/home/joaovitor/Documents/ForPaper/data/fs_541_1.mtx", "/home/joaovitor/Documents/ForPaper/data/bp_200.mtx", "/home/joaovitor/Documents/ForPaper/data/dwt_503.mtx"};


    for(int inst=0; inst<filenames_list.size();inst++){
        
        int v1, v2, NE, NV;

        vector<pair<int,int>> OD;

        ifstream f_inst(filenames_list.at(inst));

        if (!f_inst.is_open())
        {
            cout << "ERROR: File " << filenames_list.at(inst) << " not found!" << endl;
            exit(0);
        }

        f_inst>>NV;
        f_inst>>NE;

        for(int i=0; i<NE; ++i){
            
            f_inst>> v1;
            f_inst>> v2;
            if(v1!=v2){
                OD.emplace_back(make_pair(v1,v2));
            }
        }
        //numero de vertices e numero de arestas
        //cout<<NV<<" "<<NE<<endl;
        Graph G(NV);

        for (int i = 0; i < NV; ++i)
            add_edge(OD[i].first, OD[i].second, G);

        graph_traits< Graph >::vertex_iterator ui, ui_end;

        property_map< Graph, vertex_degree_t >::type deg = get(vertex_degree, G);

        for (boost::tie(ui, ui_end) = vertices(G); ui != ui_end; ++ui)
            deg[*ui] = degree(*ui, G);

        property_map< Graph, vertex_index_t >::type index_map = get(vertex_index, G);

        cout << "=================================================================================" <<std::endl;
        cout << "  " <<std::endl;

        std::cout << "Filename: " << filenames_list.at(inst) << std::endl;
        instances.emplace_back(filenames_list.at(inst));
        std::cout << "original bandwidth: " << bandwidth(G) << std::endl;
        original_bandwitch.emplace_back(bandwidth(G));

        std::vector< Vertex > inv_perm(num_vertices(G));
        std::vector< size_type > perm(num_vertices(G));


         {
            // reverse cuthill_mckee_ordering
            cuthill_mckee_ordering( G, inv_perm.rbegin(), get(vertex_color, G), make_degree_map(G));
            cout << "Reverse Cuthill-McKee ordering:" << endl;
            cout << "  " <<std::endl;
            

            for (std::vector< Vertex >::const_iterator i = inv_perm.begin(); i != inv_perm.end(); ++i)
                cout << index_map[*i] << " ";
            cout << std::endl;

            for (size_type c = 0; c != inv_perm.size(); ++c)
                perm[index_map[inv_perm[c]]] = c;

            std::cout << "  bandwidth: "
                      << bandwidth(G, make_iterator_property_map( &perm[0], index_map, perm[0]))
                      << std::endl;
            
            final_bandwitch.emplace_back(bandwidth(G, make_iterator_property_map( &perm[0], index_map, perm[0])));
        }

        write_csv("three_cols.csv", columns, instances, original_bandwitch, final_bandwitch);

    }
    return 0;
}   