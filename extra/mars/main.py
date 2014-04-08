transit_daily_mSv = 1.9
martian_surface_daily_mSv = .7
travel_time_days = 270
days_on_mars = 90
#
def calc_transit_radiation(transit_daily_mSv,travel_time_days):
	return flight_time_daily_mSv * travel_time_days
#
def calc_marian_surface_radiation(martian_surface_daily_mSv,days_on_mars):
	return martian_surface_daily_mSv * days_on_mars
#
def calc_total_radiation(transit_radiation,surface_radiation):
	return transit_radiation + surface_radiation
#
print calc_total_radiation(calc_transit_radiation(transit_daily_mSv,travel_time_days),calc_marian_surface_radiation(martian_surface_daily_mSv,days_on_mars))