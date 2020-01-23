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

def main( args ):
    foreach_sims3pack( args )

def foreach_sims3pack( args ):
    if os.path.isdir( args.path ):
        files = os.listdir( args.path )
    else:
        files = [ args.path ]

    for f in files:
        if 'sims3pack' not in f:
            continue
        if args.verbose: print( 'Processing {0}'.format( f ) )
        data = open_sims3pack( f )
        if args.debug: peek_header( data )
        xml = extract_xml( data )
        dbpf = extract_dbpf( data )
        package_name = f.replace( 'sims3pack', 'package' )
        out_path = os.path.join( args.out, package_name )
        print( 'Writing {inf} as {outf}'.format( inf = f, outf = out_path ) )
        with open( out_path, 'wb' ) as out:
             out.write( dbpf )


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser( description='sims3pack to package tool' )
    parser.add_argument( 'path', help = 'sims3pack file or path to dir with simspack files' )
    parser.add_argument( '-o', '--out', help = 'path to Mods folder', default = '.' )
    parser.add_argument( '-v', '--verbose', action="store_true", help="Increase the verbosity." )
    parser.add_argument( '-g', '--debug',   action="store_true", help="Debug output." )

    args = parser.parse_args()
    main( args )
