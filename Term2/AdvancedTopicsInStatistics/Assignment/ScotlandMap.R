ScotlandMap <- function(data, figtitle="",lower=NULL,upper=NULL){
  # local authority administrative areas
  names <- c("Skye-Lochalsh", "Banff-Buchan",  "Caithness",     "Berwickshire",  "Ross-Cromarty", "Orkney",        "Moray" ,       
  "Shetland",      "Lochaber",      "Gorden",        "Western Isles", "Sutherland",    "Nairn",         "Wigtown",      
  "NE Fife",       "Kincardine",    "Bedenoch",      "Ettrick",       "Inverness",     "Roxburgh",      "Angus",        
  "Aberdeen",      "Argyll-Bute",   "Clydesdale",    "Kirkcaldy" ,    "Dunfermline",   "Nithsdale",     "East Lothian", 
  "Perth-Kinross", "West Lothian",  "Cumnock-Doon",  "Stewartry",     "Midlothian",    "Stirling",      "Kyle-Carrick", 
  "Inverclyde",    "Cunninghame",   "Monklands",     "Dumbarton",     "Clydebank",     "Renfrew",       "Falkirk" ,     
  "Clackmannan",   "Motherwell",    "Edinburgh",     "Kilmarnock",    "East Kilbride" ,"Hamilton",      "Glasgow",      
  "Dundee" ,       "Cumbernauld",   "Bearsden" ,     "Eastwood" ,    "Strathkelvin",  "Tweeddale" ,    "Annandale") 
  
  # merging provided data with area names
  df <- data.frame(Name=names,Value = data)
  
  # Reading in Scotland shapefiles
  Scotland <- readOGR(dsn = '.',
                      layer = 'Scotland')
  
  # Combining data and the shapefile
  Scotland_data <- merge(Scotland, df,
               by = 'Name')
  Scotland_data <- st_as_sf(Scotland_data)
  
  # Setting the colour limits
  if(is.null(lower)) lower=floor(min(data))
  if(is.null(upper)) upper=ceiling(max(data))
  
  # Creating the map
  ggplot(Scotland_data,
         aes(fill = Value)) +
    geom_sf(colour = NA) + theme_bw() +
    labs(x = 'Longitude',
         y = 'Latitude',
         fill = 'Value') +
    scale_fill_gradientn(colours = brewer.pal(9, 'RdPu'),
                         breaks = seq(lower,upper,length.out=5)) +
    ggtitle(label=figtitle)
}
