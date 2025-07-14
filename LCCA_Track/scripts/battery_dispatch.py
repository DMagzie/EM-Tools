def rule_based_dispatch(load_profile, pv_profile, battery_capacity_kwh, max_kw, round_trip_eff=0.9):
    battery_soc = 0
    dispatch = []
    for load, pv in zip(load_profile, pv_profile):
        net = pv - load
        if net > 0:
            charge = min(net, max_kw, battery_capacity_kwh - battery_soc)
            battery_soc += charge * round_trip_eff
            dispatch.append(-charge)
        else:
            discharge = min(-net, max_kw, battery_soc)
            battery_soc -= discharge / round_trip_eff
            dispatch.append(discharge)
    return dispatch
