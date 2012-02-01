require 'yaml'

$VERBOSE=nil

config_yml = YAML.load_file "#{File.dirname(__FILE__)}/../config.yml"
throw "Unable to read the config file at #{File.dirname(__FILE__)}/../config.yml" unless config_yml!=nil

# First argument is assumed to be the input file. 
#
original_input_file=ARGV[0]

# Before doing anything we append ".pep.xml" to the input file name because peptide prophet can't handle anything else
# In order for this to work properly the file actually needs to be copied temporarily to the new .pep.xml location
#
cmd = "/bin/cp #{original_input_file} #{original_input_file}.pep.xml; "

cmd << "#{config_yml['protk_path']}/protein_prophet.rb"


ARGV[0]="#{original_input_file}.pep.xml"

ARGV.each { |a| 
  cmd << " #{a}" 
}

# Cleans up the .pep.xml input file which was used temporarily
#
cmd << "; /bin/rm #{original_input_file}.pep.xml"

#p cmd


%x[#{cmd}]

