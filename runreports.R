#The folder containing all of the .rmds and the custom_current.css need to be in the folder
#defined in list.files(here()), in this example that folder is "pagedown"
#the folder listed in line 9 in output_dir, needs to be an already created folder where you want the
#output .pdfs and .htmls to reside
library(pagedown)
library(here)
template_file <- 'Templates/NY14_template_es.Rmd'
cat( "template file is ", template_file, "\n" )
filenames2 = list.files(here(), pattern = ".Rmd")
print(filenames2)
file_count = length(filenames2)
for (x in filenames2) {
  print(x)
  if ( x == template_file ){
    next
  }
  pagedown::chrome_print(rmarkdown::render(
  here(x), envir = new.env(),clean = TRUE, output_dir = (here("Outputs"))))
}

#left to do: how to get it to move into the GH pages branch - and discriminate based on file extenstion
#(pdf vs html)

