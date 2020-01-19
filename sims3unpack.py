#!/usr/bin/env python
import os, sys
import pdb

def open_sims3pack( fname ):
    data = None
    with open( fname, 'rb' ) as f:
        data = f.read()
    return data
    
def peek_header( data ):
    xml_key = '<?xml'
    dbpf_key = 'DBPF'
    print( '{xml} key starts at: {loc}'.format( xml = xml_key, loc = data.find( xml_key ) ) )
    print( '{xml} key starts at: {loc}'.format( xml = dbpf_key, loc = data.find( dbpf_key ) ) )

def extract_xml( data ):
    xml_start  = data.find( '<?xml' )
    dbpf_start = data.find( 'DBPF'  )
    return( data[ xml_start : dbpf_start ] )

def extract_dbpf( data ):
    dbpf_start = data.find( 'DBPF' )
    return( data[ dbpf_start: ] )

def main():
    print( 'hello' )
    files = os.listdir( '.' )
    for f in files:
        data = open_sims3pack( f )
        peek_header( data )
        xml = extract_xml( data )
        dbpf = extract_dbpf( data )
        package_name = f.replace( 'sims3pack', 'package' )
        print( 'Writing {inf} as {outf}'.format( inf = f, outf = package_name ) )
        with open( package_name, 'wb' ) as out:
             out.write( dbpf )

if __name__ == '__main__':
    main()
