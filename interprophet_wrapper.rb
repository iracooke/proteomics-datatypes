require 'pathname'

$VERBOSE=nil

actual_output_path_string=ARGV[0]

wd= Dir.pwd

original_input_files=ARGV.drop(1)
cmd=""

output_substitution_cmds=""

input_files=original_input_files.collect do |input|

  # We append ".pep.xml" to the input file name because interprophet can't handle anything else
  # In order for this to work properly we need to create a symbolic link our working directory
  #
  original_input_path=Pathname.new("#{input}")
  actual_input_path_string="#{wd}/#{original_input_path.basename}.pep.xml"

  cmd << "ln -s #{input} #{actual_input_path_string};"
  output_substitution_cmds << "ruby -pi -e \"gsub('#{actual_input_path_string}', '#{input}.pep.xml')\" interprophet_output.pep.xml;"
  actual_input_path_string
end

interprophet_path=%x[which interprophet.rb]
cmd << interprophet_path.chomp

input_files.each { |input|
  cmd << " #{input}"
}


cmd << " -o interprophet_output.pep.xml -r"

cmd << ";#{output_substitution_cmds}"

p cmd

%x[#{cmd}]

