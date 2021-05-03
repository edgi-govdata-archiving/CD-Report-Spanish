from csv import reader
import sys, argparse
import pdb

def main( argv ):
    parser = argparse.ArgumentParser( prog='make_state_sedfiles_es.py', 
       description=\
       'Make a sedfile for each of the States in the input CSV,' \
       ' and a make_reports_es.sh that will call the sedfiles' )
    parser.add_argument( '-c', '--todo_file', required=True,
        help='The states to work with' )
    parser.add_argument( '-s', '--states_file', required=True,
        help='The state names' )
    my_args = parser.parse_args()

    states_todo_file = my_args.todo_file
    states_file = my_args.states_file

    template_filename = "AK_template_es.Rmd"
    template_state = "Alaska"
    template_state_uc = "ALASKA"
    template_st = "AK"
    template_data_date = "091820"
    data_date = "102320"
    bash_name = "make_reports_es.sh"
    
    with open( states_todo_file, 'r' ) as read_obj:
        csv_reader = reader( read_obj )
        states = list( map( tuple, csv_reader ))
    with open( states_file, 'r' ) as read_obj:
        csv_reader = reader( read_obj )
        state_name_list = list( map( tuple, csv_reader ))
    state_names = {}
    state_names_uc = {}
    for state_abbr, state_name in state_name_list:
        state_names[ state_abbr ] = state_name
        state_names_uc[ state_abbr ] = state_name.upper()
    with open( bash_name, "w" ) as bash_obj:
        # pdb.set_trace()
        for state_x in states:
            state = state_x[0]
            target_file = "New/{}_2020_es.Rmd".format( state )
            sed_name = "SEDs/sedfile_{}_es.txt".format( state )
            with open( sed_name, "w" ) as write_obj:
                str = "s/{}/{}/g\n".format( template_state, state_names[ state ] )
                write_obj.write( str )
                str = "s/{}/{}/g\n".format( template_state_uc, state_names_uc[ state ])
                write_obj.write( str )
                str = "s/AK/{}/g\n".format( state )
                write_obj.write( str )
                if ( template_data_date != data_date ):
                    str = "s/{}/{}\n".format( template_data_date, data_date )
                    write_obj.write( str )
            str = "sed -f {} {} > {}\n".format( sed_name, template_filename,
                                                target_file )
            bash_obj.write( str ) 

if __name__ == "__main__":
    main( sys.argv[1:] )


