"""
Proteomics format classes
"""
import logging
import re
from galaxy.datatypes.data import *
from galaxy.datatypes.xml import *
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

class PepXml(GenericXml):
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

class MzML( GenericXml ):
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


class ProtXML( Text ):
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



class MzXML( Text ):
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
 
class Mgf( Text ):
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
            
                
class MascotDat( Text ):
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


class RAW( Binary ):
    """Class describing a Thermo Finnigan binary RAW file"""
    file_ext = "raw"
    def sniff( self, filename ):
        # Thermo Finnigan RAW format is proprietary and hence not well documented.
        # Files start with 2 bytes that seem to differ followed by F\0i\0n\0n\0i\0g\0a\0n
        # This combination represents 17 bytes, but to play safe we read 20 bytes from 
        # the start of the file.
        try:
            header = open( filename ).read(20)
            hexheader = binascii.b2a_hex( header )
            finnigan  = binascii.hexlify( 'F\0i\0n\0n\0i\0g\0a\0n' )
            if hexheader.find(finnigan) != -1:
                return True
            return False
        except:
            return False
    def set_peek( self, dataset, is_multi_byte=False ):
        if not dataset.dataset.purged:
            dataset.peek  = "Thermo Finnigan RAW file"
            dataset.blurb = data.nice_size( dataset.get_size() )
        else:
            dataset.peek = 'file does not exist'
            dataset.blurb = 'file purged from disk'
    def display_peek( self, dataset ):
        try:
            return dataset.peek
        except:
            return "Thermo Finnigan RAW file (%s)" % ( data.nice_size( dataset.get_size() ) )


if hasattr(Binary, 'register_sniffable_binary_format'):
    Binary.register_sniffable_binary_format('RAW', 'RAW', RAW)


class Msp(Text):
    """ Output of NIST MS Search Program chemdata.nist.gov/mass-spc/ftp/mass-spc/PepLib.pdf """
    file_ext = "msp"
    
    @staticmethod
    def next_line_starts_with(contents, prefix):
        next_line = contents.readline()
        return next_line != None and next_line.startswith(prefix)

    def sniff(self, filename):
        """ Determines whether the file is a NIST MSP output file. 

        >>> fname = get_test_fname('test.msp')  
        >>> Msp().sniff(fname)
        True
        >>> fname = get_test_fname('test.mzXML')
        >>> Msp().sniff(fname)
        False
        """
        with open(filename, 'r') as contents:
            return Msp.next_line_starts_with(contents, "Name:") and Msp.next_line_starts_with(contents, "MW:")

class Ms2(Text):
    file_ext = "ms2"
    
    def sniff(self, filename):
        """ Determines whether the file is a valid ms2 file. 

        >>> fname = get_test_fname('test.msp')  
        >>> Ms2().sniff(fname)
        False
        >>> fname = get_test_fname('test.ms2')
        >>> Ms2().sniff(fname)
        True
        """

        with open(filename, 'r') as contents:
            header_lines = []
            while True:
                line = contents.readline()
                if line == None or len(line) == 0:
                    pass
                elif line.startswith('H\t'):
                    header_lines.append(line)
                else:
                    break
        for header_field in ['CreationDate', 'Extractor', 'ExtractorVersion', 'ExtractorOptions']:
            found_header = False
            for header_line in header_lines:
                if header_line.startswith('H\t%s' % (header_field)):
                    found_header = True
                    break
            if not found_header:
                return False

        return True

# unsniffable binary format, should do something about this
class XHunterAslFormat(Binary):
    """ Annotated Spectra in the HLF format http://www.thegpm.org/HUNTER/format_2006_09_15.html """
    file_ext = "hlf"


if hasattr(Binary, 'register_unsniffable_binary_ext'):
    Binary.register_unsniffable_binary_ext('hlf')
