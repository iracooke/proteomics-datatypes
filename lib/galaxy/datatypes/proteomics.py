"""
Proteomics format classes
"""
import data
import logging
import xml
import re
from galaxy.datatypes.sniff import *
from galaxy.datatypes.binary import *

log = logging.getLogger(__name__)


class Xls( Binary ):
    """Class describing a binary excel spreadsheet file"""
    file_ext = "xls"

    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek  = "Excel Spreadsheet file"
            dataset.blurb = data.nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'
    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Binary xls file (%s)" % ( data.nice_size( dataset.get_size() ) )

class PepXml(xml.GenericXml):
    """pepXML data"""
    file_ext = "pepxml"

    def set_peek( self, dataset, is_multi_byte=False ):
        """Set the peek and blurb text"""
        if not dataset.dataset.purged:
            dataset.peek = data.get_file_peek( dataset.file_name, is_multi_byte=is_multi_byte )
            dataset.blurb = 'pepXML data'
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'
    def sniff( self, filename ):
        """
        Determines whether the file is pepXML
        """
        #TODO - Use a context manager on Python 2.5+ to close handle
        handle = open(filename)
        xmlns_re = re.compile(".*pepXML\"")
        for i in range(3):
            line = handle.readline()
            if xmlns_re.match(line.strip()):
                handle.close()
                return True

        handle.close()
        return False

class MzML( xml.GenericXml ):
    """mzML data"""
    file_ext = "mzml"
    
    def set_peek( self, dataset, is_multi_byte=False ):
        """Set the peek and blurb text"""
        if not dataset.dataset.purged:
            dataset.peek = data.get_file_peek( dataset.file_name, is_multi_byte=is_multi_byte )
            dataset.blurb = 'mzML Mass Spectrometry data'
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'

    def sniff( self, filename ):
        handle = open(filename)
        xmlns_re = re.compile("^<mzML")
        for i in range(3):
            line = handle.readline()
            if xmlns_re.match(line.strip()):
                handle.close()
                return True

        handle.close()
        return False


class ProtXML( data.Text ):
    """protXML data"""
    file_ext = "protxml"

    def set_peek( self, dataset, is_multi_byte=False ):
        """Set the peek and blurb text"""
        if not dataset.dataset.purged:
            dataset.peek = data.get_file_peek( dataset.file_name, is_multi_byte=is_multi_byte )
            dataset.blurb = 'prot XML Search Results'
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'
    def sniff( self, filename ):
        protxml_header = [ '<?xml version="1.0" encoding="ISO-8859-1"?>',
        'xmlns="http://regis-web.systemsbiology.net/protXML"' ]

        for i, line in enumerate( file( filename ) ):
            if i >= len( pepxml_header ):
                return True
            line = line.rstrip( '\n\r' )
            if protxml_header[ i ] not in line:
                return False



class MzXML( data.Text ):
    """mzXML data"""
    file_ext = "mzXML"

    def set_peek( self, dataset, is_multi_byte=False ):
        """Set the peek and blurb text"""
        if not dataset.dataset.purged:
            dataset.peek = data.get_file_peek( dataset.file_name, is_multi_byte=is_multi_byte )
            dataset.blurb = 'mzXML Mass Spectrometry data'
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'
    def sniff( self, filename ):
        mzxml_header = [ '<?xml version="1.0" encoding="ISO-8859-1"?>',
        '<mzXML xmlns="http://sashimi.sourceforge.net/schema_revision/mzXML_2.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://sashimi.sourceforge.net/schema_revision/mzXML_2.1 http://sashimi.sourceforge.net/schema_revision/mzXML_2.1/mzXML_idx_2.1.xsd">' ]
        for i, line in enumerate( file( filename ) ):
            if i >= len( mzxml_header ):
                return True
            line = line.rstrip( '\n\r' )
            if line != mzxml_header[ i ]:
                return False        
 
class Mgf( data.Text ):
    """Mascot Generic Format data"""
    file_ext = "mgf"

    def set_peek( self, dataset, is_multi_byte=False ):
        """Set the peek and blurb text"""
        if not dataset.dataset.purged:
            dataset.peek = data.get_file_peek( dataset.file_name, is_multi_byte=is_multi_byte )
            dataset.blurb = 'mgf Mascot Generic Format'
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'


    def sniff( self, filename ):
        mgf_begin_ions = "BEGIN IONS"
        max_lines=100

        for i, line in enumerate( file( filename ) ):
            line = line.rstrip( '\n\r' )
            if line==mgf_begin_ions:
                return True
            if i>max_lines:
                return False
                
class MascotDat( data.Text ):
    """Mascot search results """
    file_ext = "mascotdat"

    def set_peek( self, dataset, is_multi_byte=False ):
        """Set the peek and blurb text"""
        if not dataset.dataset.purged:
            dataset.peek = data.get_file_peek( dataset.file_name, is_multi_byte=is_multi_byte )
            dataset.blurb = 'mascotdat Mascot Search Results'
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'


    def sniff( self, filename ):
        mime_version = "MIME-Version: 1.0 (Generated by Mascot version 1.0)"
        max_lines=10

        for i, line in enumerate( file( filename ) ):
            line = line.rstrip( '\n\r' )
            if line==mime_version:
                return True
            if i>max_lines:
                return False
