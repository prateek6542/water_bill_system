def calculate_bill(units, has_sewer, months):
    # Slab limits
    slab1_limit = 20
    slab2_limit = 30

    # Rates
    rate1 = 19.30
    rate2 = 33.28
    rate3 = 59.90

    # Slab calculations
    slab1_units = min(units, slab1_limit)
    slab2_units = min(max(units - slab1_limit, 0), slab2_limit - slab1_limit)
    slab3_units = max(units - slab2_limit, 0)

    cost1 = slab1_units * rate1
    cost2 = slab2_units * rate2
    cost3 = slab3_units * rate3

    subtotal = cost1 + cost2 + cost3

    # Sewer charge
    sewer_charge = subtotal * 0.30 if has_sewer else 0

    # Fixed charge
    # fixed_charge = 110

    # Total bill for 1 month
    total_one_month = subtotal + sewer_charge + fixed_charge

    # Multiply by number of months
    final_total = total_one_month * months

    return {
        'slab1_units': slab1_units,
        'slab2_units': slab2_units,
        'slab3_units': slab3_units,
        'cost1': cost1,
        'cost2': cost2,
        'cost3': cost3,
        'subtotal': subtotal,
        'sewer_charge': sewer_charge,
        # 'fixed_charge': fixed_charge,
        'total_one_month': total_one_month,
        'months': months,
        'final_total': final_total,
        'has_sewer': has_sewer
    }
