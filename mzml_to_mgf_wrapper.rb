require 'yaml'

$VERBOSE=nil

config_yml = YAML.load_file "#{File.dirname(__FILE__)}/../config.yml"
throw "Unable to read the config file at #{File.dirname(__FILE__)}/../config.yml" unless config_yml!=nil

cmd = "#{config_yml['protk_path']}/file_convert.rb"

ARGV.each { |a| 
  cmd << " #{a}" 
}

#p cmd

%x[sh #{cmd} ]
