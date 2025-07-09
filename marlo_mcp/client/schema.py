from typing import List, Literal, Optional, Union
import uuid
from pydantic import BaseModel, Field
from enum import Enum

class EmissionZoneEnum(str, Enum):
    ECA = "ECA"
    NORMAL = "Normal"

class OwnershipEnum(str, Enum):
    OWNED = "OV - Owned Vessel"
    TCIN = "tcin"
    OTHER = "other"

class FuelTypeEnum(str, Enum):
    HSFO = "HSFO"
    VLSFO = "VLSFO"
    ULSFO = "ULSFO"
    MGO = "MGO"
    LNG = "LNG"

class BulkCarrierSubType(str, Enum):
    Handysize = "Handysize"
    Handymax = "Handymax"
    Supramax = "Supramax"
    Ultramax = "Ultramax"
    Panamax = "Panamax"
    Kamsarmax = "Kamsarmax"
    PostPanamax = "Post-Panamax"
    Capesize = "Capesize"


class TankerSubType(str, Enum):
    Handysize = "Handysize"
    Panamax = "Panamax"
    Aframax = "Aframax"
    Suezmax = "Suezmax"
    VLCC = "VLCC"
    ULCC = "ULCC"


class ActivityEnum(str, Enum):
    LOADING = "Loading"
    DISCHARGING = "Discharging"
    IDLE = "Idle"


class BunkerTanker(BaseModel):
    capacity: Optional[float] = Field(None, description="Tank capacity")
    description: Optional[str] = Field(None, description="Tank description")
    location: Optional[str] = Field(None, description="Tank location")
    tank_number: Optional[float] = Field(None, description="Tank number")
    unit: Optional[str] = Field(None, description="Capacity unit")

class DwtDraft(BaseModel):
    dwt: Optional[float] = Field(None, description="Deadweight tonnage")
    draft: Optional[float] = Field(None, description="Draft measurement")
    displaced: Optional[float] = Field(None, description="Displaced volume")
    tons_per_centimeter: Optional[float] = Field(None, description="Tons per centimeter immersion")
    remarks: Optional[str] = Field(None, description="Additional remarks")

class LoadDischargePerfs(BaseModel):
    max_liquid_pressure: Optional[float] = Field(None, description="Maximum liquid pressure")
    min_gas_pressure: Optional[float] = Field(None, description="Minimum gas pressure")
    min_gas_return: Optional[float] = Field(None, description="Minimum gas return pressure")
    min_liquid_pressure: Optional[float] = Field(None, description="Minimum liquid pressure")
    time: Optional[float] = Field(None, description="Operation time")
    type: Optional[str] = Field(None, description="Operation type")

class PortConsumptions(BaseModel):
    auxil_fuel_consumption: Optional[float] = Field(None, description="Auxiliary fuel consumption")
    boiler_fuel_consumption: Optional[float] = Field(None, description="Boiler fuel consumption")
    bunker_safety_margin: Optional[float] = Field(None, description="Bunker safety margin")
    clean_fuel_consumption: Optional[float] = Field(None, description="Clean fuel consumption")
    cool_fuel_consumption: Optional[float] = Field(None, description="Cool fuel consumption")
    discharge_consumption: Optional[float] = Field(None, description="Discharge fuel consumption")
    fuel_capacity: Optional[float] = Field(None, description="Fuel capacity")
    fuel_grade: Optional[str] = Field(None, description="Fuel grade")
    fuel_type: Optional[str] = Field(None, description="Fuel type")
    heat_fuel_consumption: Optional[float] = Field(None, description="Heat fuel consumption")
    heat1_fuel_consumption: Optional[float] = Field(None, description="Heat 1 fuel consumption")
    heat2_fuel_consumption: Optional[float] = Field(None, description="Heat 2 fuel consumption")
    idle_off_fuel_consumption: Optional[float] = Field(None, description="Idle off fuel consumption")
    idle_on_fuel_consumption: Optional[float] = Field(None, description="Idle on fuel consumption")
    igs_fuel_consumption: Optional[float] = Field(None, description="IGS fuel consumption")
    incinerator: Optional[float] = Field(None, description="Incinerator fuel consumption")
    loading_consumption: Optional[float] = Field(None, description="Loading fuel consumption")
    maneuv_fuel_consumption: Optional[float] = Field(None, description="Maneuvering fuel consumption")
    unit: Optional[str] = Field(None, description="Consumption unit")

class ResidualTankInformation(BaseModel):
    stowage_type: Optional[str] = Field(None, description="Stowage type")
    tank_capacity: Optional[float] = Field(None, description="Tank capacity")
    tank_coating: Optional[str] = Field(None, description="Tank coating")
    tank_location: Optional[str] = Field(None, description="Tank location")
    tank_name: Optional[str] = Field(None, description="Tank name")
    tank_number: Optional[float] = Field(None, description="Tank number")
    tank_type: Optional[str] = Field(None, description="Tank type")

class Routes(BaseModel):
    block: Optional[bool] = Field(None, description="Block status")
    func: Optional[str] = Field(None, description="Function")
    hide: Optional[bool] = Field(None, description="Hide status")
    no_tolls: Optional[bool] = Field(None, description="No tolls flag")
    pd: Optional[float] = Field(None, description="PD value")
    region_id: Optional[str] = Field(None, description="Region ID")
    toll_ballast: Optional[float] = Field(None, description="Toll ballast")
    toll_laden: Optional[float] = Field(None, description="Toll laden")
    use: Optional[str] = Field(None, description="Usage")
    xp: Optional[float] = Field(None, description="XP value")

class FuelDataEntries(BaseModel):
    fuel_type: Optional[FuelTypeEnum] = Field(None, description="Fuel type")
    consumption: Optional[float] = Field(None, description="Fuel consumption")

class SpeedConsumptions(BaseModel):
    ballast_or_laden: Optional[str] = Field(None, description="Ballast or laden status")
    consumption_type: Optional[str] = Field(None, description="Consumption type")
    engine_load: Optional[float] = Field(None, description="Engine load")
    speed: Optional[float] = Field(None, description="Speed")
    default: Optional[bool] = Field(None, description="Default flag")
    fuel_data: Optional[List[FuelDataEntries]] = Field([], description="Fuel data entries")

class StopTankInformation(BaseModel):
    stowage_type: Optional[str] = Field(None, description="Stowage type")
    tank_capacity: Optional[float] = Field(None, description="Tank capacity")
    tank_coating: Optional[str] = Field(None, description="Tank coating")
    tank_location: Optional[str] = Field(None, description="Tank location")
    tank_name: Optional[str] = Field(None, description="Tank name")
    tank_number: Optional[float] = Field(None, description="Tank number")
    tank_type: Optional[str] = Field(None, description="Tank type")

class StowageCraneInfo(BaseModel):
    crane_capacity: Optional[float] = Field(None, description="Crane capacity")
    crane_outreach: Optional[float] = Field(None, description="Crane outreach")
    crane_radius: Optional[float] = Field(None, description="Crane radius")
    crane_type: Optional[str] = Field(None, description="Crane type")

class StowageHatchInfo(BaseModel):
    hatch_cement_holes: Optional[float] = Field(None, description="Hatch cement holes")
    hatch_cement_holes_dimension: Optional[float] = Field(None, description="Hatch cement holes dimension")
    hatch_crane_capacity: Optional[float] = Field(None, description="Hatch crane capacity")
    hatch_derrick_capacity: Optional[float] = Field(None, description="Hatch derrick capacity")
    hatch_length: Optional[float] = Field(None, description="Hatch length")
    hatch_max_weight: Optional[float] = Field(None, description="Hatch maximum weight")
    hatch_number: Optional[float] = Field(None, description="Hatch number")
    hatch_width: Optional[float] = Field(None, description="Hatch width")
    hatch_wlthc: Optional[float] = Field(None, description="Hatch WLTHC")

class StowageHoldInfo(BaseModel):
    ballast_hold: Optional[bool] = Field(False, description="Ballast hold flag")
    hold_capacity_bale: Optional[float] = Field(None, description="Hold capacity for bale")
    hold_capacity_grain: Optional[float] = Field(None, description="Hold capacity for grain")
    hold_length: Optional[float] = Field(None, description="Hold length")
    hold_number: Optional[float] = Field(None, description="Hold number")
    hold_tank_weight_capacity: Optional[float] = Field(None, description="Hold tank weight capacity")
    hold_weight_capacity: Optional[float] = Field(None, description="Hold weight capacity")
    hold_width: Optional[float] = Field(None, description="Hold width")
    hold_width_aft: Optional[float] = Field(None, description="Hold width aft")
    hold_width_fwd: Optional[float] = Field(None, description="Hold width forward")

class TankInformation(BaseModel):
    stowage_type: Optional[str] = Field(None, description="Stowage type")
    tank_capacity: Optional[float] = Field(None, description="Tank capacity")
    tank_coating: Optional[str] = Field(None, description="Tank coating")
    tank_location: Optional[str] = Field(None, description="Tank location")
    tank_name: Optional[str] = Field(None, description="Tank name")
    tank_number: Optional[float] = Field(None, description="Tank number")
    tank_type: Optional[str] = Field(None, description="Tank type")

class TceTarget(BaseModel):
    effective_from_gmt: Optional[str] = Field(None, description="Effective from GMT timestamp")
    tce_target: Optional[float] = Field(None, description="TCE target value")

class VesselFuel(BaseModel):
    aux_engine_fuel_type: Optional[FuelTypeEnum] = Field(None, description="Auxiliary engine fuel type")
    boiler_fuel_type: Optional[FuelTypeEnum] = Field(None, description="Boiler fuel type")
    emission_zone: Optional[EmissionZoneEnum] = Field(None, description="Emission control area zone")
    main_engine_fuel_type: Optional[FuelTypeEnum] = Field(None, description="Main engine fuel type")

class PortConsumptionNormal(BaseModel):
    activity: Optional[ActivityEnum] = Field(None, description="Port activity type")
    aux_engine_consumption: Optional[float] = Field(None, description="Auxiliary engine fuel consumption")
    boiler_consumption: Optional[float] = Field(None, description="Boiler fuel consumption")
    main_engine_consumption: Optional[float] = Field(None, description="Main engine fuel consumption")

class PortConsumptionEca(BaseModel):
    eca_activity: Optional[ActivityEnum] = Field(None, description="ECA port activity type")
    eca_aux_engine_consumption: Optional[float] = Field(None, description="ECA auxiliary engine fuel consumption")
    eca_main_engine_consumption: Optional[float] = Field(None, description="ECA main engine fuel consumption")
    eca_boiler_consumption: Optional[float] = Field(None, description="ECA boiler fuel consumption")

class SpeedConsumptionNormal(BaseModel):
    aux_engine_consumption: Optional[float] = Field(None, description="Auxiliary engine fuel consumption at speed")
    ballast_or_laden: Optional[str] = Field(None, description="Ballast or laden condition")
    boiler_engine_consumption: Optional[float] = Field(None, description="Boiler engine fuel consumption at speed")
    default: Optional[bool] = Field(None, description="Default speed consumption flag")
    main_engine_consumption: Optional[float] = Field(None, description="Main engine fuel consumption at speed")
    speed: Optional[float] = Field(None, description="Vessel speed in knots")

class SpeedConsumptionEca(BaseModel):
    eca_aux_engine_consumption: Optional[float] = Field(None, description="ECA auxiliary engine fuel consumption at speed")
    eca_ballast_or_laden: Optional[str] = Field(None, description="ECA ballast or laden condition")
    eca_boiler_engine_consumption: Optional[float] = Field(None, description="ECA boiler engine fuel consumption at speed")
    eca_default: Optional[bool] = Field(None, description="ECA default speed consumption flag")
    eca_main_engine_consumption: Optional[float] = Field(None, description="ECA main engine fuel consumption at speed")
    eca_speed: Optional[float] = Field(None, description="ECA vessel speed in knots")

class CreateVesselSchema(BaseModel):
    bale: Optional[float] = Field(0, description="Bale capacity of the vessel in metric tons")
    beam: Optional[float] = Field(0, description="Beam width of the vessel in meters")
    year_of_build: Optional[int] = Field(0, description="Year when the vessel was built (yyyy)")
    beaufort: Optional[str] = Field("", description="Beaufort wind force scale description")
    beaufort_scale: Optional[int] = Field(0, description="Beaufort wind force scale number (0-12)")
    bridge_number: Optional[str] = Field("", description="Bridge number identifier")
    build_details: Optional[str] = Field("", description="Detailed information about vessel construction")
    builder: Optional[str] = Field("", description="Name of the shipyard that built the vessel")
    bunker_tanker: Optional[List[BunkerTanker]] = Field([], description="List of bunker tanker information")
    callsign: Optional[str] = Field("", description="International radio call sign of the vessel")
    cargo_or_gear: Optional[str] = Field("", description="Type of cargo or gear equipment")
    ccr_number: Optional[str] = Field("", description="CCR (Continuous Certificate of Registry) number")
    cellular: Optional[str] = Field("", description="Cellular phone number for vessel communication")
    classification_soceity: Optional[str] = Field("", description="Classification society that certified the vessel")
    public_company_id: Optional[str] = Field(None, description="Public company identifier")
    constants_lakes: Optional[float] = Field(0, description="Vessel constants for lake operations")
    constants_sea: Optional[float] = Field(0, description="Vessel constants for sea operations")
    cross_reference_number: Optional[str] = Field("", description="Cross reference number for vessel identification")
    daily_cost: Optional[float] = Field(..., description="Daily operating cost of the vessel")
    date_of_build: Optional[str] = Field(None, description="Date when the vessel was built")
    deadweight: Optional[float] = Field(..., description="Deadweight tonnage of the vessel")
    deck_capacity: Optional[float] = Field(0, description="Deck cargo capacity in metric tons")
    dem_analyst: Optional[str] = Field("", description="DEM analyst assigned to the vessel")
    depth: Optional[float] = Field(0, description="Depth of the vessel in meters")
    displacement_at_design: Optional[float] = Field(0, description="Vessel displacement at design draft")
    displacement_at_summer: Optional[float] = Field(0, description="Vessel displacement at summer draft")
    displacement_fresh_water: Optional[float] = Field(0, description="Vessel displacement in fresh water")
    displacement_lightship: Optional[float] = Field(0, description="Lightship displacement")
    displacement_normal_ballast: Optional[float] = Field(0, description="Displacement in normal ballast condition")
    displacement_tropical_fw: Optional[float] = Field(0, description="Displacement in tropical fresh water")
    displacement_tropical_sw: Optional[float] = Field(0, description="Displacement in tropical salt water")
    displacement_winter: Optional[float] = Field(0, description="Displacement in winter condition")
    draft_at_design: Optional[float] = Field(0, description="Draft at design condition")
    draft_at_summer: Optional[float] = Field(0, description="Draft at summer condition")
    draft_fresh_water: Optional[float] = Field(0, description="Draft in fresh water")
    draft_lightship: Optional[float] = Field(0, description="Draft in lightship condition")
    draft_normal_ballast: Optional[float] = Field(0, description="Draft in normal ballast condition")
    draft_tropical_fw: Optional[float] = Field(0, description="Draft in tropical fresh water")
    draft_tropical_sw: Optional[float] = Field(0, description="Draft in tropical salt water")
    draft_winter: Optional[float] = Field(0, description="Draft in winter condition")
    dwt_at_design: Optional[float] = Field(0, description="Deadweight at design condition")
    dwt_at_summer: Optional[float] = Field(0, description="Deadweight at summer condition")
    dwt_date: Optional[str] = Field(None, description="Date of deadweight measurement")
    dwt_draft: Optional[List[DwtDraft]] = Field(..., description="List of deadweight-draft relationships")
    dwt_fresh_water: Optional[float] = Field(0, description="Deadweight in fresh water")
    dwt_lightship: Optional[float] = Field(0, description="Deadweight in lightship condition")
    dwt_normal_ballast: Optional[float] = Field(0, description="Deadweight in normal ballast condition")
    dwt_tropical_fw: Optional[float] = Field(0, description="Deadweight in tropical fresh water")
    dwt_tropical_sw: Optional[float] = Field(0, description="Deadweight in tropical salt water")
    dwt_winter: Optional[float] = Field(0, description="Deadweight in winter condition")
    email: Optional[str] = Field("", description="Email address for vessel communication")
    engine_make: Optional[str] = Field("", description="Manufacturer of the main engine")
    ex_vessel_name: Optional[str] = Field("", description="Previous name of the vessel")
    fax: Optional[str] = Field("", description="Fax number for vessel communication")
    freeboard_at_design: Optional[float] = Field(0, description="Freeboard at design condition")
    freeboard_at_summer: Optional[float] = Field(0, description="Freeboard at summer condition")
    freeboard_fresh_water: Optional[float] = Field(0, description="Freeboard in fresh water")
    freeboard_lightship: Optional[float] = Field(0, description="Freeboard in lightship condition")
    freeboard_normal_ballast: Optional[float] = Field(0, description="Freeboard in normal ballast condition")
    freeboard_tropical_fw: Optional[float] = Field(0, description="Freeboard in tropical fresh water")
    freeboard_tropical_sw: Optional[float] = Field(0, description="Freeboard in tropical salt water")
    freeboard_winter: Optional[float] = Field(0, description="Freeboard in winter condition")
    fresh_water: Optional[float] = Field(0, description="Fresh water capacity")
    gap_value: Optional[str] = Field("", description="Gap value for cargo operations")
    grabs_capacity: Optional[float] = Field(0, description="Capacity of cargo grabs in metric tons")
    grabs_quantity: Optional[float] = Field(0, description="Quantity of cargo grabs")
    grain: Optional[float] = Field(0, description="Grain capacity in cubic meters")
    grt_int: Optional[float] = Field(0, description="International gross tonnage")
    h_and_m_value: Optional[str] = Field("", description="H&M (Hull and Machinery) value")
    hatch_type: Optional[str] = Field("", description="Type of cargo hatches")
    hull_number: Optional[str] = Field("", description="Hull number from shipyard")
    hull_type: Optional[str] = Field("", description="Type of hull construction")
    ice_class: Optional[str] = Field("", description="Ice class certification")
    imo: Optional[str] = Field("", description="International Maritime Organization number")
    last_dry_dock: Optional[str] = Field(None, description="Date of last dry dock")
    last_hull_cleaning: Optional[str] = Field(None, description="Date of last hull cleaning")
    last_prop_polished: Optional[str] = Field(None, description="Date of last propeller polishing")
    length_overall: Optional[float] = Field(0, description="Overall length of the vessel in meters")
    lightship: Optional[float] = Field(0, description="Lightship weight in metric tons")
    load_discharge_perfs: Optional[List[LoadDischargePerfs]] = Field([], description="Loading and discharging performance data")
    manager: Optional[str] = Field("", description="Vessel manager name")
    manager_id: Optional[str] = Field("", description="Vessel manager identifier")
    master_phone: Optional[str] = Field("", description="Master's phone number")
    max_draft: Optional[float] = Field(0, description="Maximum draft in meters")
    mini_m: Optional[str] = Field("", description="Mini M value")
    name: Optional[str] = Field(..., description="Vessel name")
    net_tonnage_panama: Optional[float] = Field(0, description="Panama Canal net tonnage")
    net_tonnage_suez: Optional[float] = Field(0, description="Suez Canal net tonnage")
    next_dry_dock: Optional[str] = Field(None, description="Date of next scheduled dry dock")
    next_inspection: Optional[str] = Field(None, description="Date of next inspection")
    next_survey: Optional[str] = Field(None, description="Date of next survey")
    nrt_int: Optional[float] = Field(0, description="International net register tonnage")
    official_number: Optional[str] = Field("", description="Official registration number")
    opa_90: Optional[float] = Field(0, description="OPA 90 value")
    operator: Optional[str] = Field("", description="Vessel operator name")
    others: Optional[float] = Field(0, description="Other miscellaneous values")
    owner: Optional[str] = Field("", description="Vessel owner name")
    ownership: Optional[OwnershipEnum] = Field(..., description="Vessel ownership structure or type")
    p_and_i_club: Optional[str] = Field("", description="P&I club membership information")
    panama_gross: Optional[float] = Field(0, description="Panama gross tonnage")
    pns_number: Optional[str] = Field("", description="PNS number")
    pool_point: Optional[str] = Field("", description="Pool point")
    propeller_pitch: Optional[float] = Field(None, description="Propeller pitch")
    registry: Optional[uuid.UUID] = Field(None, description="Registry")
    residual_tank_information: Optional[List[ResidualTankInformation]] = Field([], description="Residual tank information")
    routes: Optional[List[Routes]] = Field([], description="Routes")
    salt_water_summer_draft: Optional[float] = Field(0, description="Salt water summer draft")
    sat_a: Optional[str] = Field("", description="SAT A")
    sat_b: Optional[str] = Field("", description="SAT B")
    sat_c: Optional[str] = Field("", description="SAT C")
    scrubber: Optional[str] = Field("", description="Scrubber")
    sea_state: Optional[str] = Field("", description="Sea state")
    sea_state_scale: Optional[int] = Field(0, description="Sea state scale")
    sea_swell: Optional[str] = Field("", description="Sea swell")
    sea_swell_scale: Optional[int] = Field(0, description="Sea swell scale")
    stop_tank_information: Optional[List[StopTankInformation]] = Field([], description="Stop tank information")
    stowage_crane_info: Optional[List[StowageCraneInfo]] = Field([], description="Stowage crane information")
    stowage_hatch_info: Optional[List[StowageHatchInfo]] = Field([], description="Stowage hatch information")
    stowage_hold_info: Optional[List[StowageHoldInfo]] = Field([], description="Stowage hold information")
    suez_gross: Optional[float] = Field(0, description="Suez gross tonnage")
    suez_vessel_type: Optional[str] = Field("", description="Suez vessel type")
    tank_information: Optional[List[TankInformation]] = Field([], description="Tank information")
    tce_target: Optional[List[TceTarget]] = Field([], description="TCE target")
    technical_manager: Optional[str] = Field(None, description="Technical manager")
    telex: Optional[str] = Field("", description="Telex")
    tpc: Optional[float] = Field(0, description="TPC")
    tpc_at_design: Optional[float] = Field(0, description="TPC at design")
    tpc_at_summer: Optional[float] = Field(0, description="TPC at summer")
    tpc_fresh_water: Optional[float] = Field(0, description="TPC in fresh water")
    tpc_lightship: Optional[float] = Field(0, description="TPC in lightship condition")
    tpc_normal_ballast: Optional[float] = Field(0, description="TPC in normal ballast condition")
    tpc_tropical_fw: Optional[float] = Field(0, description="TPC in tropical fresh water")
    tpc_tropical_sw: Optional[float] = Field(0, description="TPC in tropical salt water")
    tpc_winter: Optional[float] = Field(0, description="TPC in winter condition")
    trade_area: Optional[str] = Field("", description="Trade area")
    tve_expires: Optional[str] = Field(None, description="TVE expires")
    type_code: Optional[Literal['Bulk Carrier', 'Tanker']] = Field(..., description="Type code")
    type_dwt: Optional[Union[BulkCarrierSubType, TankerSubType]] = Field(..., description="Type DWT")
    ventilation: Optional[str] = Field("", description="Ventilation")
    vessel_code: Optional[str] = Field("", description="Vessel code")
    vessel_flag: Optional[str] = Field("", description="Vessel flag")
    vessel_fleet: Optional[str] = Field("", description="Vessel fleet")
    vessel_remarks: Optional[str] = Field("", description="Vessel remarks")
    vessel_type_corr: Optional[float] = Field(0, description="Vessel type correction")
    winter_draft: Optional[float] = Field(0, description="Winter draft")
    yard: Optional[str] = Field(None, description="Yard")
    yard_id: Optional[int] = Field(0, description="Yard ID")
    clone_from: Optional[str] = Field("", description="Clone from")
    vessel_fuel: Optional[List[VesselFuel]] = Field([], description="Vessel fuel")
    port_consumption_normal: Optional[List[PortConsumptionNormal]] = Field([], description="Port consumption normal")
    port_consumption_eca: Optional[List[PortConsumptionEca]] = Field([], description="Port consumption ECA")
    speed_consumption_normal: Optional[List[SpeedConsumptionNormal]] = Field(..., description="Speed consumption normal - requires at least two values (laden and ballast) with one marked as default")
    speed_consumption_eca: Optional[List[SpeedConsumptionEca]] = Field([], description="Speed consumption ECA - requires at least two values (laden and ballast) with one marked as default")
    use_normal_port_consumption_in_eca: Optional[bool] = Field(True, description="Use normal port consumption in ECA")
    use_normal_speed_consumption_in_eca: Optional[bool] = Field(True, description="Use normal speed consumption in ECA")
