from csv import reader
import sys, argparse
import pdb

def main( argv ):
    parser = argparse.ArgumentParser( prog='make_sedfiles_es.py', 
       description=\
       'Make a sedfile for each of the CDs/States in the input CSV,' \
       ' and a make_reports_es.sh that will call the sedfiles' )
    parser.add_argument( '-c', '--cds_file', required=True,
        help='The CDs to work with' )
    parser.add_argument( '-s', '--states_file', required=True,
        help='The state names' )
    parser.add_argument( '-t', '--template_file', required=True,
        help='The Rmd file to use as template' )
    my_args = parser.parse_args()

    # pdb.set_trace()
    cds_todo_file = my_args.cds_file
    states_file = my_args.states_file
    template_filename = my_args.template_file

    template_state_cd = "14\$^\\\\circ\$ distrito de New York"
    template_state_cd_uc = "14\$^\\\\circ\$ DISTRITO DE NEW YORK"
    state_cd_new = "$^\\\\circ$ distrito de "
    state_cd_new_uc = "$^\\\\circ$ DISTRITO DE "
    template_st = "NY"
    template_data_date = "102320"
    data_date = "111820"
    bash_name = "make_reports_es.sh"
    
    with open( cds_todo_file, 'r' ) as read_obj:
        csv_reader = reader( read_obj )
        state_cds = list( map( tuple, csv_reader ))
    with open( states_file, 'r' ) as read_obj:
        csv_reader = reader( read_obj )
        state_name_list = list( map( tuple, csv_reader ))
    state_names = {}
    state_names_uc = {}
    for state_abbr, state_name in state_name_list:
        state_names[ state_abbr ] = state_name
        state_names_uc[ state_abbr ] = state_name.upper()
    with open( bash_name, "w" ) as bash_obj:
        for state, cd in state_cds:
            target_file = "New/{}{}_2020_es.Rmd".format( state, cd )
            cd = int( cd )
            sed_name = "SEDs/sedfile_{}{}_es.txt".format( state, cd )
            with open( sed_name, "w" ) as write_obj:
                str = "s/{}/{}{}{}/g\n".format( template_state_cd,
                     cd, state_cd_new, state_names[ state ])
                write_obj.write( str )
                str = "s/{}/{}{}{}/g\n".format( template_state_cd_uc,
                     cd, state_cd_new_uc, state_names_uc[ state ])
                write_obj.write( str )
                str = "s/NY 14/{} {}/g\n".format( state, cd )
                write_obj.write( str )
                str = "s/_NY-14/_{}-{}/g\n".format( state, cd )
                write_obj.write( str )
                str = "s/NY14/{}{}/g\n".format( state, cd )
                write_obj.write( str )
                str = "s/_NY-/_{}-/g\n".format( state )
                write_obj.write( str )
                if ( template_data_date != data_date ):
                    str = "s/{}/{}/g\n".format( template_data_date, data_date )
                    write_obj.write( str )
            str = "sed -f {} {} > {}\n".format( sed_name, template_filename,
                                                target_file )
            bash_obj.write( str ) 

if __name__ == "__main__":
    main( sys.argv[1:] )


