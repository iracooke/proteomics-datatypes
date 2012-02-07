require 'optparse'
require 'ostruct'
require 'pathname'

$VERBOSE=nil


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


wd= Dir.pwd

original_input_files=ARGV
cmd=""

input_files=original_input_files.collect do |input|

  # We append ".pep.xml" to the input file name because interprophet can't handle anything else
  # In order for this to work properly we need to create a symbolic link our working directory
  #
  original_input_path=Pathname.new("#{input}")
  actual_input_path_string="#{wd}/#{original_input_path.basename}.pep.xml"

  cmd << "ln -s #{input} #{actual_input_path_string};"
  actual_input_path_string
end

interprophet_path=%x[which interprophet.rb]
cmd << interprophet_path.chomp

input_files.each { |input|
  cmd << " #{input}"
}


cmd << " -o #{@options.explicit_output} -r"

%x[#{cmd}]

