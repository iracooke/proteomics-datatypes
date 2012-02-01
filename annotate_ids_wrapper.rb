require 'yaml'

$VERBOSE=nil

config_yml = YAML.load_file "#{File.dirname(__FILE__)}/../config.yml"
throw "Unable to read the config file at #{File.dirname(__FILE__)}/../config.yml" unless config_yml!=nil

# First argument is assumed to be the input file. 
#

cmd = "#{config_yml['protk_path']}/annotate_ids.rb"

ARGV.each { |a| 
  cmd << " #{a}" 
}

#p cmd

result=%x[sh #{cmd} ]

