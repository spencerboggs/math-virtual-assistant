
import os
import sys

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m")

    print("███╗░░░███╗░█████╗░████████╗██╗░░██╗")
    print("████╗░████║██╔══██╗╚══██╔══╝██║░░██║")
    print("██╔████╔██║███████║░░░██║░░░███████║")
    print("██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║")
    print("██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║")
    print("╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝")
    print("Multifunctional Academic Task Helper")
    print("\033[0m")

    selection = input("What kind of problem would you like to solve?\n")
    solution_found = False

    print()

    # AMINO ACID SEQUENCE FROM RNA OR DNA
    amino_acid_keywords = ["amino", "acid", "protein", "sequence", "rna", "dna"]
    if sum(keyword in selection.lower() for keyword in amino_acid_keywords) >= 2:
        confirm = input("Are you trying to convert RNA or DNA to amino acid sequence? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.aminoseq as aminoseq
            solution_found = True

    # BINARY TO DECIMAL CONVERSION
    binary_keywords = ["binary", "decimal", "convert"]
    if sum(keyword in selection.lower() for keyword in binary_keywords) >= 2:
        confirm = input("Are you trying to convert binary and decimal? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.bintodec as bintodec
            solution_found = True

    # BITWISE OPERATIONS
    bitwise_keywords = ["bitwise", "operation", "and", "or", "xor", "not"]
    if sum(keyword in selection.lower() for keyword in bitwise_keywords) >= 2:
        confirm = input("Are you trying to perform bitwise operations on 2 binary values? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.bitwise as bitwise
            solution_found = True

    # BOOLEAN ALGEBRA
    boolean_keywords = ["boolean", "algebra", "simplify", "expression"]
    if sum(keyword in selection.lower() for keyword in boolean_keywords) >= 2:
        confirm = input("Are you trying to simplify a boolean expression? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.boolean as boolean
            solution_found = True
    
    # CENTROID CALCULATION
    centroid_keywords = ["centroid", "coordinates"]
    if sum(keyword in selection.lower() for keyword in centroid_keywords) >= 1:
        confirm = input("Are you trying to calculate the centroid of a set of coordinates? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.centroid as centroid
            solution_found = True


    # CIRCULAR MOTION
    circular_keywords = ["circular", "motion", "velocity", "acceleration"]
    if sum(keyword in selection.lower() for keyword in circular_keywords) >= 2:
        confirm = input("Are you trying to calculate the velocity or acceleration of an object in circular motion? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.circlmot as circlmot
            solution_found = True

    # CIRCUIT VOLATAGE
    circuit_voltage_keywords = ["circuit", "voltage"]
    if sum(keyword in selection.lower() for keyword in circuit_voltage_keywords) >= 2:
        confirm = input("Are you trying to calculate the voltage, current, or resistance in a circuit? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.circuitv as circuitv
            solution_found = True

    # COMBINATION CALCULATION
    combination_keywords = ["combination", "nCr", "combines"]
    if sum(keyword in selection.lower() for keyword in combination_keywords) >= 1:
        confirm = input("Are you trying to calculate the combination of nCr? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.combines as combines
            solution_found = True

    # COMPOUND INTEREST
    compound_interest_keywords = ["compound", "interest"]
    if sum(keyword in selection.lower() for keyword in compound_interest_keywords) >= 2:
        confirm = input("Are you trying to calculate the time or final value of a compound interest? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.compound as compound
            solution_found = True

    # LAW OF COOLING
    cooling_keywords = ["cooling", "law", "cool", "time", "temperature", "object", "ambient", "room", "constant"]
    if sum(keyword in selection.lower() for keyword in cooling_keywords) >= 2:
        confirm = input("Are you trying to calculate the temperature of an object using the law of cooling? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.cooling as cooling
            solution_found = True

    # COULOMB'S LAW
    coulomb_keywords = ["coulomb", "law", "force", "two", "object"]
    if sum(keyword in selection.lower() for keyword in coulomb_keywords) >= 2:
        confirm = input("Are you trying to calculate the force between two charges using Coulomb's law? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.coulomb as coulomb
            solution_found = True

    # CPI AND MIPS CALCULATION
    cpi_mips_keywords = ["cpi", "mips", "clock", "rate", "instruction", "count", "execution", "time"]
    if sum(keyword in selection.lower() for keyword in cpi_mips_keywords) >= 2:
        confirm = input("Are you trying to calculate the clock rate, instruction count, execution time, CPI, or MIPS? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.cpimips as cpimips
            solution_found = True

    # ESCAPE VELOCITY
    escape_velocity_keywords = ["escape", "velocity", "leave"]
    if sum(keyword in selection.lower() for keyword in escape_velocity_keywords) >= 2:
        confirm = input("Are you trying to calculate the escape velocity of an object? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.escapev as escapev
            solution_found = True

    # EULER'S METHOD
    euler_keywords = ["euler", "method"]
    if sum(keyword in selection.lower() for keyword in euler_keywords) >= 1:
        confirm = input("Are you trying to calculate the value of y using Euler's method? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.eulerslv as eulerslv
            solution_found = True

    # EXPONENTIAL GROWTH
    exponential_growth_keywords = ["exponential", "growth"]
    if sum(keyword in selection.lower() for keyword in exponential_growth_keywords) >= 1:
        confirm = input("Are you trying to calculate the final value of an exponential growth? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.exgrowth as exgrowth
            solution_found = True

    # GRAVITATIONAL ENERGY
    grav_energy_keywords = ["gravitational", "energy", "GPE"]
    if sum(keyword in selection.lower() for keyword in grav_energy_keywords) >= 2:
        confirm = input("Are you trying to calculate the gravitational potential energy? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.gravengy as gravengy
            solution_found = True

    # IMPULSE CALCULATION
    impulse_keywords = ["impulse"]
    if sum(keyword in selection.lower() for keyword in impulse_keywords) >= 1:
        confirm = input("Are you trying to calculate the impulse? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.impulse as impulse
            solution_found = True

    # INERTIA CALCULATION
    inertia_keywords = ["inertia"]
    if sum(keyword in selection.lower() for keyword in inertia_keywords) >= 1:
        confirm = input("Are you trying to calculate the inertia of an object? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.inertia as inertia
            solution_found = True

    # KINEMATIC EQUATIONS
    kinematic_keywords = ["kinematic", "equation", "velocity", "acceleration", "time", "distance"]
    if sum(keyword in selection.lower() for keyword in kinematic_keywords) >= 1:
        confirm = input("Are you trying to calculate the velocity, acceleration, or time using the kinematic equations? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.kinesolv as kinesolv
            solution_found = True

    # LAGRANGE ERROR BOUND
    lagrange_keywords = ["lagrange", "error", "bound"]
    if sum(keyword in selection.lower() for keyword in lagrange_keywords) >= 1:
        confirm = input("Are you trying to calculate the Lagrange error bound? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.lagrange as lagrange
            solution_found = True

    # LEAST SQUARES REGRESSION
    least_squares_keywords = ["least", "squares", "regression"]
    if sum(keyword in selection.lower() for keyword in least_squares_keywords) >= 2:
        confirm = input("Are you trying to calculate the value of y using least squares regression? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.leastsqr as leastsqr
            solution_found = True

    # MATRIX CALCULATIONS
    matrix_keywords = ["matrix", "add", "subtract", "multiply", "determinant", "inverse", "transpose"]
    if sum(keyword in selection.lower() for keyword in matrix_keywords) >= 2:
        confirm = input("Are you trying to perform calculations on a matrix? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.matrix as matrix
            solution_found = True

    # MIDPOINT CALCULATION
    midpoint_keywords = ["midpoint", "coordinates"]
    if sum(keyword in selection.lower() for keyword in midpoint_keywords) >= 2:
        confirm = input("Are you trying to calculate the midpoint of a set of coordinates? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.midpoint as midpoint
            solution_found = True

    # MIPS TO ASM
    mips_asm_keywords = ["mips", "asm", "convert", "machine", "code"]
    if sum(keyword in selection.lower() for keyword in mips_asm_keywords) >= 2:
        confirm = input("Are you trying to convert MIPS assembly to machine code? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.mipsasm as mipsasm
            solution_found = True

    # ORBITAL ENERGY
    orbital_energy_keywords = ["orbital", "energy"]
    if sum(keyword in selection.lower() for keyword in orbital_energy_keywords) >= 1:
        confirm = input("Are you trying to calculate the orbital energy? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.orbiteng as orbiteng
            solution_found = True

    # PARAMETRIC EQUATION PLOTTER
    parametric_keywords = ["parametric", "equation", "plot", "x(t)", "y(t)"]
    if sum(keyword in selection.lower() for keyword in parametric_keywords) >= 2:
        confirm = input("Are you trying to plot a parametric equation? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.paraplot as paraplot
            solution_found = True

    # PARTIAL FRACTION DECOMPOSITION
    partial_fraction_keywords = ["partial", "fraction", "decomposition"]
    if sum(keyword in selection.lower() for keyword in partial_fraction_keywords) >= 2:
        confirm = input("Are you trying to perform partial fraction decomposition? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.partial as partial
            solution_found = True

    # PENDULUM PERIOD CALCULATION
    pendulum_keywords = ["pendulum", "period"]
    if sum(keyword in selection.lower() for keyword in pendulum_keywords) >= 2:
        confirm = input("Are you trying to calculate the period of a pendulum? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.pendulum as pendulum
            solution_found = True

    # PERMUTATION CALCULATION
    permutation_keywords = ["permutation", "nPr", "permutes", "permutations"]
    if sum(keyword in selection.lower() for keyword in permutation_keywords) >= 1:
        confirm = input("Are you trying to calculate the permutation of nPr? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.permutes as permutes
            solution_found = True

    # PHYSICS ELECTRICS AND MAGNETICS EQUATIONS
    physics_electromag_keywords = ["physics", "electric", "magnetic", "equation", "equations", "μ"]
    if sum(keyword in selection.lower() for keyword in physics_electromag_keywords) >= 2:
        confirm = input("Do you want to see relevant electric and magnetic equations? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.physicse as physicse
            solution_found = True

    # PHYSICS MECHANICS EQUATIONS
    physics_mechanics_keywords = ["physics", "mechanic", "equation"]
    if sum(keyword in selection.lower() for keyword in physics_mechanics_keywords) >= 2:
        confirm = input("Do you want to see relevant mechanics equations? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.physicsm as physicsm
            solution_found = True

    # POLAR TO CARTESIAN CONVERSION
    polar_cartesian_keywords = ["polar", "cartesian", "convert", "θ"]
    if sum(keyword in selection.lower() for keyword in polar_cartesian_keywords) >= 2:
        confirm = input("Are you trying to convert polar to cartesian coordinates? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.poltocar as poltocar
            solution_found = True

    # PROJECTILE MOTION
    projectile_keywords = ["projectile", "motion", "θ"]
    if sum(keyword in selection.lower() for keyword in projectile_keywords) >= 2:
        confirm = input("Are you trying to calculate the velocity, time, or position of a projectile? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.projmotn as projmotn
            solution_found = True

    # SEQUENCE CALCULATION
    sequence_keywords = ["sequence", "nth", "term"]
    if sum(keyword in selection.lower() for keyword in sequence_keywords) >= 1:
        confirm = input("Are you trying to calculate the nth term of a sequence? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.sequence as sequence
            solution_found = True

    # SERIES CALCULATION
    series_keywords = ["series", "sum"]
    if sum(keyword in selection.lower() for keyword in series_keywords) >= 1:
        confirm = input("Are you trying to calculate the sum of a series? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.series as series
            solution_found = True

    # SIMPSON'S RULE
    simpson_keywords = ["simpson", "rule"]
    if sum(keyword in selection.lower() for keyword in simpson_keywords) >= 2:
        confirm = input("Are you trying to calculate the integral using Simpson's rule? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.simpsons as simpsons
            solution_found = True

    # SLOPE FIELD PLOTTER
    slope_field_keywords = ["slope", "field", "plot", "y'"]
    if sum(keyword in selection.lower() for keyword in slope_field_keywords) >= 2:
        confirm = input("Are you trying to plot a slope field? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.slopefld as slopefld
            solution_found = True

    # SPRING WORK CALCULATION
    spring_work_keywords = ["spring", "work"]
    if sum(keyword in selection.lower() for keyword in spring_work_keywords) >= 2:
        confirm = input("Are you trying to calculate the work done by a spring? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.sprngwrk as sprngwrk
            solution_found = True

    # TAYLOR SERIES CALCULATION
    taylor_series_keywords = ["taylor", "series", "f(x)"]
    if sum(keyword in selection.lower() for keyword in taylor_series_keywords) >= 2:
        confirm = input("Are you trying to calculate the Taylor series of a function? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.taylor as taylor
            solution_found = True

    # TORQUE CALCULATION
    torque_keywords = ["torque", "τ"]
    if sum(keyword in selection.lower() for keyword in torque_keywords) >= 2:
        confirm = input("Are you trying to calculate the torque? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.torque as torque
            solution_found = True

    # TRAPEZOIDAL RULE
    trapezoidal_keywords = ["trapezoidal", "rule"]
    if sum(keyword in selection.lower() for keyword in trapezoidal_keywords) >= 2:
        confirm = input("Are you trying to calculate the integral using the trapezoidal rule? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.traprule as traprule
            solution_found = True

    # TRUTH TABLE GENERATOR
    truth_table_keywords = ["truth", "table", "generate", "expression"]
    if sum(keyword in selection.lower() for keyword in truth_table_keywords) >= 2:
        confirm = input("Are you trying to generate a truth table for a boolean expression? (yes/no)\n")
        if confirm.lower() != "no" and confirm.lower() != "n":
            import scripts.truthtab as truthtab
            solution_found = True

    if not solution_found:
        print("No solution found for the given input. Please check your spelling.")
        input("Press [Enter] to continue")


    main()

main()