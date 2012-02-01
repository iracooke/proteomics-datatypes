require 'yaml'
require 'optparse'
require 'ostruct'

$VERBOSE=nil

config_yml = YAML.load_file "#{File.dirname(__FILE__)}/../config.yml"
throw "Unable to read the config file at #{File.dirname(__FILE__)}/../config.yml" unless config_yml!=nil


@options = OpenStruct.new
@options.library = []
@options.inplace = false
@options.encoding = "utf8"
@options.transfer_type = :auto
@options.verbose = false

@option_parser=OptionParser.new do |opts|
  
  
  
  @options.explicit_output = nil
  opts.on( '-o', '--output out', 'An explicitly named output file.' ) do |out|
    @options.explicit_output = out
  end  
   
  opts.on( '-h', '--help', 'Display this screen' ) do
    puts opts
    exit
  end
        
end

@option_parser.parse!

original_input_files=ARGV
cmd=""

input_files=original_input_files.collect do |input|

  # We append ".pep.xml" to the input file name because interprophet can't handle anything else
  # In order for this to work properly the file actually needs to be copied temporarily to the new .pep.xml location
  #
  cmd << "/bin/cp #{input} #{input}.pep.xml; "
  "#{input}.pep.xml"
end


cmd << "#{config_yml['protk_path']}/interprophet.rb"

input_files.each { |input|
  cmd << " #{input}"
}


cmd << " -o #{@options.explicit_output} -r"

# Clean up the .pep.xml input files which were used temporarily
#
input_files.each { |input_file|
  cmd << "; /bin/rm #{input_file}"
}

%x[#{cmd}]

