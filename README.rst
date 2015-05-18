Proteomics Datatypes
====================

Support for a proteomics and mass spectrometry datatypes for Galaxy_

.. _Galaxy: http://galaxyproject.org/


Included Datatypes
------------------

================      =====================  =======     ====================================
Class                 Extension              Sniffer     Application or Purpose
================      =====================  =======     ====================================
Binary                cps                    False       SearchGUI_ / PeptideShaker_
PepXML_               raw_pepxml             True        TPP_ Search Engine Outputs
PepXML_               peptideprophet_pepxml  True        TPP_ PeptideProphet Outputs
PepXML_               interprophet_pepxml    True        TPP_ iProphet Outputs
ProtXML_              protxml                True        TPP_ ProteinProphet Outputs
GenericXML            trafoxml               False       OpenMS_ RT Transforms
GenericXML            qcml_                  False       OpenMS_ QC Data
PepXmlReport          pepxml.tsv             False       Tabular PepXML
ProtXmlReport         protxml.tsv            False       Tabular ProtXML
MascotDat             mascotdat              False       Raw Mascot Search Results
MzML_                 mzml                   True        Raw Mass Spec Data
Mgf                   mgf                    True        MS/MS Spectra
IdpDB                 idpdb                  False       
Wiff                  wiff                   False       Raw Mass Spec Data
MzXML                 mzxml                  True        Raw Mass Spec Data
MzQuantML_            mzq                    True        HUPO standard for quant data
MzIdentML_            mzid                   True        HUPO standard for ID data
TraML_                traml                  True        HUPO standard for transition lists
FeatureXML            featurexml             False       OpenMS_
ConsensusXML          consensusxml           False       OpenMS_
IdXML                 idxml                  False       OpenMS_
TandemXML_            tandem                 False       XTandem output
RAW                   raw                    False       Raw Mass Spec Data
Msp_                  msp                    True        Spectral Library
SPLib_                splib 				 True		 Spectral Library
Ms2                   ms2                    False       MS/MS Spectra
XHunterAslFormat      hlf                    False       Spectral Library
================      =====================  =======     ====================================


.. _qcml: http://code.google.com/p/qcml
.. _PepXML: http://tools.proteomecenter.org/wiki/index.php?title=Formats:pepXML
.. _ProtXML: http://tools.proteomecenter.org/wiki/index.php?title=Formats:protXML
.. _TPP: http://tools.proteomecenter.org/wiki/index.php?title=Software:TPP
.. _OpenMS: https://github.com/OpenMS/OpenMS
.. _SearchGUI: https://code.google.com/p/searchgui/
.. _PeptideShaker: https://code.google.com/p/peptide-shaker/
.. _MzML: http://www.psidev.info/mzml_1_0_0%20
.. _MzQuantML: http://www.psidev.info/mzquantml
.. _MzIdentML: http://www.psidev.info/mzidentml
.. _TraML: http://www.psidev.info/traml
.. _TandemXML: http://www.thegpm.org/docs/X_series_output_form.pdf
.. _Msp: http://chemdata.nist.gov/mass-spc/ftp/mass-spc/PepLib.pdf
.. _SPLib: http://tools.proteomecenter.org/wiki/index.php?title=Software:SpectraST#Developer.27s_Guide

Visualization
-------------

This package also installs display applications for mzML, PepXML and ProtXML formats. These are designed to work with the protviz_ web application.  Configuring this application requires a fair number of extra steps though.  See the protviz_ documentation for more info.  

.. _protviz: https://bitbucket.org/Andrew_Brock/proteomics-visualise

