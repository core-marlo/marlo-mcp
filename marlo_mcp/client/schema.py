import uuid
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, List, Optional, Union, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


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
    eca_aux_engine_consumption: Optional[float] = Field(None,
                                                        description="ECA auxiliary engine fuel consumption at speed")
    eca_ballast_or_laden: Optional[str] = Field(None, description="ECA ballast or laden condition")
    eca_boiler_engine_consumption: Optional[float] = Field(None,
                                                           description="ECA boiler engine fuel consumption at speed")
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
    load_discharge_perfs: Optional[List[LoadDischargePerfs]] = Field([],
                                                                     description="Loading and discharging performance data")
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
    residual_tank_information: Optional[List[ResidualTankInformation]] = Field([],
                                                                               description="Residual tank information")
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
    speed_consumption_normal: Optional[List[SpeedConsumptionNormal]] = Field(...,
                                                                             description="Speed consumption normal - requires at least two values (laden and ballast) with one marked as default")
    speed_consumption_eca: Optional[List[SpeedConsumptionEca]] = Field([],
                                                                       description="Speed consumption ECA - requires at least two values (laden and ballast) with one marked as default")
    use_normal_port_consumption_in_eca: Optional[bool] = Field(True, description="Use normal port consumption in ECA")
    use_normal_speed_consumption_in_eca: Optional[bool] = Field(True, description="Use normal speed consumption in ECA")


class CreateEstimateSheetSchema(BaseModel):
    name: Optional[str] = None


class PaymentTypeEnum(str, Enum):
    DAILY_RATE = "Daily Rate"
    LUMPSUM = "Lumpsum"
    PER_UNIT = "Per Unit"


class RebillableCategoryChoicesEnum(str, Enum):
    ADVANCE_REBILLABLE = "Advance Rebillable"
    NON_REBILLABLE = "Non-Rebillable"
    REBILLABLE = "Rebillable"


class CVERateTypeEnum(str, Enum):
    PER_30_DAYS = "Per 30 Days"
    AVERAGE_MONTHLY = "Average Monthly"
    MONTHLY = "Monthly"
    LUMPSUM = "Lumpsum"
    LUMPSUM_PROVISIONAL = "Lumpsum-provisional"


class CveCodeEnum(str, Enum):
    CABLE = "CABLE"
    VICTU = "VICTU"
    ALLOW = "ALLOW"
    LASHS = "LASHS"
    ILOHC = "ILOHC"
    INTHC = "INTHC"

    @property
    def category(self):
        """
        Determine the category of the CveCodeEnum instance.
        Returns:
            str: "TANKER" if the instance is either ILOHC or INTHC, otherwise "BULK".
        """
        if self in {CveCodeEnum.ILOHC, CveCodeEnum.INTHC}:
            return "BULK"
        return "TANKER"


class BrokerDetailAmountTypeEnum(str, Enum):
    ADDCOMM = "Add comm"
    BROKERAGE = "Broker"


class FreightCommissionOptionEnum(str, Enum):
    PAID_SEPARATELY = "Will be paid separately"
    DEDUCTED_FROM_INVOICE = "Deduct from invoice"
    PAID_BY_COUNTERPARTY = "Will be paid by counterparty"


class DemurrageCommissionEnum(str, Enum):
    PAID_SEPARATELY = "Will be paid separately"
    NOT_COMMISSIONABLE = "Will be paid by counterparty"
    DEDUCTED_FROM_INVOICE = "Deduct from invoice"


class FreightTypeEnum(str, Enum):
    FREIGHT_RATE = "Frt Rate"
    DAILY_RATE = "Daily Rate"
    LUMPSUM = "Lumpsum"
    WSC_FLAT = "WSC"


class PortFunctionEnum(str, Enum):
    """
    Enum class for port function
    """
    COMMENCING = 'Commencing'
    LOADING = 'Loading'
    DISCHARGING = 'Discharging'
    FUELING = 'Fueling'
    CANAL_TRANSIT = 'Canal transit'
    TERMINATING = 'Terminating'
    DELIVERY = 'Delivery'
    REDELIVERY = 'Redelivery'


class BillQuantityTypeEnum(str, Enum):
    BL_QTY = "BL Qty"
    CP_QTY = "CP Qty"
    INVOICE_QTY = "Invoice Qty"
    OUTTURN_QTY = "Outturn Qty"


class TermsFactor(str, Enum):
    """
    Enumeration of the term factors.
    """
    SHINC = 1
    SHEX0 = 1.1667
    SHEX1 = 1.2727
    SHEX2 = 1.3548
    SHEX3 = 1.4
    SHEX4 = 1.4867
    SHEX5 = 1.5
    SHEX6 = 1.6
    FHINC = 1
    FHEX0 = 1.1667
    THEX6 = 1.6
    CQD1 = 1
    SHEX7 = 0
    FHEX1 = 1.2727
    FHEX2 = 1.3548
    FHEX6 = 1.6
    FHEXUU = 0
    FHEX = 0
    THEX = 0
    FHEX7 = 0

    @classmethod
    def get_terms_factor(cls, term):
        """
        Returns the term factor for the given term.
        """
        try:
            return cls[term].value
        except KeyError:
            return 1


class CarbonEmissionFactor(str, Enum):
    """
    Enumeration of the carbon emission factors.
    """
    ethanol = 1.913
    hfo = 3.114
    ifo = 1.000
    lfo = 3.151
    lng = 2.750
    lpg_butane = 3.030
    lpg_propane = 3.000
    lsf = 3.150
    lsg = 3.000
    mdo = 1.000
    methanol = 1.375
    hsf = 1.450
    ulf = 1.360
    hsfo = 3.114
    vlsfo = 3.151
    ulsfo = 3.151
    mgo = 3.206

    @classmethod
    def get_co2_factor(cls, fuel_type):
        """
        Returns the carbon emission factor for the given fuel type.
        """
        try:
            return cls[fuel_type].value
        except KeyError:
            return 1.000


class ReductionFactor:
    def __init__(self, year, reduction_factor, phase_percentage):
        self.year = year
        self.reduction_factor = reduction_factor
        self.phase_percentage = phase_percentage


class ReductionFactorEnum(str, Enum):
    """Reduction factors for carbon calculations"""
    YEAR_2023 = ReductionFactor(2023, 5.00, 0.00)
    YEAR_2024 = ReductionFactor(2024, 7.00, 40.00)
    YEAR_2025 = ReductionFactor(2025, 9.00, 70.00)
    YEAR_2026 = ReductionFactor(2026, 11.00, 100.00)
    YEAR_2027 = ReductionFactor(2027, 0.00, 100.00)
    YEAR_2028 = ReductionFactor(2028, 0.00, 100.00)
    YEAR_2029 = ReductionFactor(2029, 0.00, 100.00)
    YEAR_2030 = ReductionFactor(2030, 0.00, 100.00)


class HireCommissionTermsEnum(str, Enum):
    PAID_SEPARATELY = "Will be paid separately"
    DEDUCTED_FROM_INVOICE = "Deduct from invoice"
    PAID_BY_COUNTERPARTY = "Will be paid by counterparty"


class ReductionFactor:
    def __init__(self, year, reduction_factor, phase_percentage):
        self.year = year
        self.reduction_factor = reduction_factor
        self.phase_percentage = phase_percentage


class ReductionFactors(str, Enum):
    """Reduction factors for carbon calculations"""
    YEAR_2023 = ReductionFactor(2023, 5.00, 0.00)
    YEAR_2024 = ReductionFactor(2024, 7.00, 40.00)
    YEAR_2025 = ReductionFactor(2025, 9.00, 70.00)
    YEAR_2026 = ReductionFactor(2026, 11.00, 100.00)
    YEAR_2027 = ReductionFactor(2027, 0.00, 100.00)
    YEAR_2028 = ReductionFactor(2028, 0.00, 100.00)
    YEAR_2029 = ReductionFactor(2029, 0.00, 100.00)
    YEAR_2030 = ReductionFactor(2030, 0.00, 100.00)


class PortData(BaseModel):
    """
    Model for PortData schema.
    """
    port_id: str = Field(description="The current port id")
    name: str = Field(description="The current Port name")
    lat: float = Field(description="The current Latitude of the Port")
    lon: float = Field(description="The current Longitude of the Port")
    speed: Optional[float] = Field(
        default=0, description="The Speed at each port.")
    port_days: Optional[float] = Field(
        default=0, description="The number of port days per port.")
    sea_days: Optional[float] = Field(
        default=0, description="The number of sea days per port.")
    distance: Optional[float] = Field(
        default=0, description="The distance travelled to reach current port.")
    arrival_time: Optional[datetime | str | None] = Field(
        default=None, description="The arrival time at current port")
    departure_time: Optional[datetime | str | None] = Field(
        default=None, description="The Departure time from current port")
    port_function: Optional[PortFunctionEnum] = Field(..., description="The current port function")
    eca_miles: Optional[float] = Field(
        default=0, description="The distance travelled in Emission Control Areas (ECA).")
    extra_port_days: Optional[float] = Field(
        default=0, description="The number of extra port days per port.")
    extra_sea_days: Optional[float] = Field(
        default=0, description="The number of extra sea days per port.")
    demurrage_days: Optional[float] = Field(
        default=0, description="The number of demurrage days per port.")

    class Config:
        json_schema_extra = {
            'example': {
                "name": "New York",
                "lat": 40.6759,
                "lon": -74.0829,
                "speed": 15,
                "port_days": 0,
                "sea_days": 0.51,
                "extra_port_days": .1,
                "extra_sea_days": 0.061,
                "distance": 176.36,
                "arrival_time": "06 Jun 2024 | 21:19",
                "departure_time": "06 Jun 2024 | 21:19",
                "port_function": "Terminating"
            }
        }


class VoyageRouteRequestSchema(BaseModel):
    """
    Model for VoyageRouteRequestSchema.
    """
    ports: List[PortData]
    seca_enabled: bool = True
    avoid_piracy: bool = False

    class Config:
        json_schema_extra = {
            'example': {
                "ports": [
                    {
                        "name": "Singapore",
                        "lat": 1.259366,
                        "lon": 103.7544,
                        "speed": 15,
                        "port_days": 0,
                        "sea_days": 0,
                        "distance": 0,
                        "arrival_time": "01 Jun 2024 | 20:00",
                        "departure_time": "01 Jun 2024 | 20:00",
                        "port_function": "Commencing"
                    }
                ]
            }
        }

    def calculate_port_sea_days_duration(self):
        """
        Calculates the duration of the voyage route sea days and port days.
        Only moves sea days, distance, and speed to the previous index.
        Port days stay with their current port.
        """
        sea_days = 0
        port_days = 0
        total_distance = 0
        total_eca_distance = 0

        # First pass: Calculate totals
        for port in self.ports:
            sea_days += port.sea_days + (port.extra_sea_days or 0)
            current_port_days = port.port_days + (port.extra_port_days or 0) + (port.demurrage_days or 0)
            port_days += current_port_days
            total_distance += port.distance or 0
            total_eca_distance += port.eca_miles or 0
            # Keep port days with current port
            port.port_days = round(current_port_days, 2)

        # Second pass: Move only sea days, distance, and speed to previous index
        for i in range(len(self.ports)):
            if i > 0:
                prev_port = self.ports[i - 1]
                curr_port = self.ports[i]
                prev_port.sea_days = round(curr_port.sea_days + (curr_port.extra_sea_days or 0), 2)
                prev_port.distance = curr_port.distance
                prev_port.speed = curr_port.speed

        # Ensure values are properly rounded and non-negative
        return {
            "sea_days": round(max(0, float(sea_days)), 2),
            "port_days": round(max(0, float(port_days)), 2),
            "distance": round(max(0, float(total_distance)), 2),
            "eca_distance": round(max(0, float(total_eca_distance)), 2),
            "non_eca_distance": round(max(0, float(total_distance - total_eca_distance)), 2),
            "duration": round(max(0, float(port_days + sea_days)), 2),
            "ports": self.ports  # Return the modified ports
        }


class VoyageSummarySchema(BaseModel):
    """
    Model for VoyageSummarySchema.
    """
    port_days: float = Field(description="Total port days")
    sea_days: float = Field(description="Total sea days")
    total_duration: float = Field(description="Total voyage duration")
    eca_distance: float = Field(description="ECA distance")
    total_distance: float = Field(description="Total distance")
    non_eca_distance: float = Field(description="Non-Eca distance")


class VoyageRouteResponseSchema(BaseModel):
    """
    Model for VoyageRouteResponseSchema.
    """
    ports: List[PortData]
    summary: VoyageSummarySchema
    waypoints: Any


class EstimateData(BaseModel):
    """
    Response schema for get estimate sheet list
    """

    estimate_count: str | None = ""
    last_updated: datetime | None = ""
    entry_date: datetime | None = ""
    last_user: str | None = ""
    worksheet_name: str | None = ""
    worksheet_type: str
    id: str | None = ""
    voyage_count: str | None = ""


class BunkerConsumptionSchema(BaseModel):
    """
    Response schema for estimate off hire
    """
    fuel_type: Optional[str]
    quantity: Optional[float]
    price: Optional[float]


class DelayBunkersSchema(BaseModel):
    """
    Response schema for estimate off hire
    """
    activity: Optional[str]
    reason: Optional[str]
    bunker_consumption: Optional[List[BunkerConsumptionSchema]]
    include_PnL: Optional[bool]


class DelayDatesSchema(BaseModel):
    activity: Optional[str]
    add_zone: Optional[float]
    deduct_zone: Optional[float]
    delay_ends: Optional[str]
    delay_hours: Optional[float]
    delay_starts: Optional[str]
    include_PnL: Optional[bool]
    reason: Optional[str]


class EstimateOffHireSchema(BaseModel):
    """
    Response schema for estimate off hire
    """
    delay_dates: Optional[List[DelayDatesSchema]]
    delay_bunkers: Optional[List[DelayBunkersSchema]]


class Waypoint(BaseModel):
    lon: float
    lat: float


class RouteData(BaseModel):
    totalDistance: Optional[float] = None
    secaDistance: Optional[float] = None
    waypoints: List[Waypoint] = None
    departure_port_id: str = ""
    destination_port_id: str = ""


class SeaMetrixRequestBody(BaseModel):
    StartLat: float
    StartLon: float
    StartPortCode: str = ""
    EndLat: float
    EndLon: float
    EndPortCode: str = ""
    AllowedAreas: List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                          16]  # NILCODE - means avoid piracy, 10001 - don't avoid piracy
    AslCompliance: int = 0
    GreatCircleInterval: int = 500
    SecaAvoidance: int = 0


class EstimateSheetSchema(BaseModel):
    company_id: Optional[str] = None
    is_active: Optional[bool] = None
    is_public: Optional[bool] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    estimate_sheet_id: Optional[str] = None


class Broker(BaseModel):
    rate: Optional[float] = 0.0
    type: Optional[BrokerDetailAmountTypeEnum] = None
    terms: Optional[HireCommissionTermsEnum] = None
    beneficiary: Optional[int] = None
    beneficiary_name: Optional[str] = None


class BunkerPlanningSchema(BaseModel):
    fuel_type: Optional[str] = None
    initial_quantity: Optional[float] = Field(default=0.0, ge=0, description="Initial quantity must be non-negative")
    initial_price: Optional[float] = 0.0
    calculation_method: Optional[str] = "FIFO"
    total_fuel_consumption: Optional[float] = 0.0

    end_price: Optional[float] = 0.0
    end_quantity: Optional[float] = 0.0

    total_port_consumption: Optional[float] = 0.0
    total_sea_consumption: Optional[float] = 0.0
    total_received_quantity: Optional[float] = 0.0

    is_initial_quantity_updated: Optional[bool] = False

    @field_validator('initial_quantity')
    def check_non_negative(cls, value):
        if value is not None and value < 0:
            raise ValueError('Initial quantity must be non-negative')
        return value


class VesselBunkerPlanningSchema(BunkerPlanningSchema):
    consumption_rate_ballast: float
    consumption_rate_discharge: float
    consumption_rate_idle: float
    consumption_rate_laden: float
    consumption_rate_load: float


class EmissionZoneSchema(BaseModel):
    fuel_type: Optional[str] = None
    initial_price: float

    consumption_rate_ballast: float
    consumption_rate_discharge: float
    consumption_rate_idle: float
    consumption_rate_laden: float
    consumption_rate_load: float

    is_price_updated: Optional[bool] = False

    @field_validator('initial_price')
    def validate_initial_price(cls, v):
        if v is None:
            return 0.0
        return v


class Co2PricePerMt(BaseModel):
    currency: str = Field(default="USD")
    value: float = Field(default=0.0)

    model_config = ConfigDict(
        from_attributes=True
    )


class ExchangeRate(BaseModel):
    currency: str = Field(default="USD")
    value: float = Field(default=0.0)

    model_config = ConfigDict(
        from_attributes=True
    )


class Cost(BaseModel):
    co2_price_per_MT: Co2PricePerMt
    exchange_rate: ExchangeRate

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def model_validate(cls, value: Any) -> 'Cost':
        if isinstance(value, dict):
            return cls(
                co2_price_per_MT=Co2PricePerMt(**value.get('co2_price_per_MT', {})),
                exchange_rate=ExchangeRate(**value.get('exchange_rate', {}))
            )
        return value


class Emission(BaseModel):
    is_port_ets_emission_changed: Optional[bool] = None
    is_sea_ets_emission_changed: Optional[bool] = None
    phase_in_percentage: Optional[float] = 0.0
    port_emission: Optional[float] = 0.0
    port_ets_emission: Optional[float] = 0.0
    port_ets_percentage: Optional[float] = 0.0
    port_function: Optional[PortFunctionEnum] = Field(..., description="The current port function")
    port_name: Optional[str] = None
    sea_emission: Optional[float] = 0.0
    sea_ets_emission: Optional[float] = 0.0
    sea_ets_percentage: Optional[float] = 0.0
    total_emission: Optional[float] = 0.0
    total_ets_emission: Optional[float] = 0.0
    total_eu_ets_exp: Optional[float] = 0.0


class UserChangedCarbon(BaseModel):
    cost: Optional[Cost] = None
    emission: Optional[List[Emission]] = None
    process: Optional[bool] = None
    total_ets_cost: Optional[float] = 0.0
    total_ets_cost_usd: Optional[float] = 0.0


class CpTerms(BaseModel):
    sequence_no: Optional[int] = 1
    cargo: None
    cargo_name: Optional[str] = None
    charterer: Optional[int] = None
    charterer_name: Optional[str] = None
    bill_by: Optional[BillQuantityTypeEnum] = None  # enum
    cargo_quantity: Optional[float] = 0.0
    cargo_unit: Optional[str] = "MT"
    cp_date: Optional[str] = None
    option_type: Optional[str] = None  # enum
    option_percentage: Optional[float] = None
    min_quantity: Optional[float] = None
    max_quantity: Optional[float] = None
    invoice_quantity: Optional[float] = None
    freight_type: Optional[str] = None  # enum
    freight_rate: Optional[float] = None
    lumpsum: Optional[float] = None
    freight_currency: Optional[str] = "USD"
    freight_exchange_rate: Optional[float] = 0.0
    commission_percentage: Optional[float] = None
    freight_tax_percent: Optional[float] = 0.0
    invoice_initial_percentage: Optional[float] = 0.0
    payment_terms_invoice_initial: Optional[str] = None  # enum
    invoice_balance_percentage: Optional[float] = 0.0
    payment_terms_invoice_balance: Optional[str] = None  # enum
    laycan_from: Optional[str] = None
    laycan_to: Optional[str] = None
    demurrage_currency: Optional[str] = None
    demurrage_exchange_rate: Optional[float] = None
    # Load and Discharge Expense details
    load_demurrage_rate: Optional[float] = None
    load_despatch_rate: Optional[float] = None
    discharge_demurrage_rate: Optional[float] = None
    discharge_despatch_rate: Optional[float] = None
    daily_rate: Optional[float] = None
    wsc_flat: Optional[float] = Field(
        default=0.0,
        description="World Scale flat rate."
    )
    wsc_percentage: Optional[float] = Field(
        default=0.0,
        description="World Scale percentage."
    )
    is_cp_terms_updated: Optional[bool] = False

    @field_validator('bill_by', mode='before')
    @classmethod
    def validate_payment_type(cls, value):
        if not value:
            return None
        return value

    @field_validator('freight_tax_percent', mode='before')
    @classmethod
    def validate_freight_tax_percent(cls, value):
        if value is None:
            return 0.0
        if not isinstance(value, (int, float)):
            raise ValueError("Freight tax percent must be a number.")
        if value < 0:
            raise ValueError("Freight tax percent cannot be negative.")
        return float(value)


class CargoData(CpTerms):
    """
    Cargo details relevant to the charter party agreement.

    Extends the CpTerms model with additional cargo-specific information.
    """
    cargo: None = None
    max_quantity: Optional[float] = Field(
        default=0.0,
        description="Maximum allowed quantity of cargo under the charter party terms."
    )
    min_quantity: Optional[float] = Field(
        default=0.0,
        description="Minimum required quantity of cargo under the charter party terms."
    )
    option_percentage: Optional[float] = Field(
        default=0.0,
        description="Percentage variation allowed in cargo quantity (used with option_type)."
    )
    option_type: Optional[str] = Field(
        default="MOLOO",
        description="Type of quantity option (e.g., MOLOO - More or Less Owner's Option)."
    )
    freight_type: Optional[FreightTypeEnum] = Field(
        default=FreightTypeEnum.FREIGHT_RATE,
        description="Type of freight calculation (Freight Rate, Daily Rate, Lumpsum, or WSC Flat)"
    )
    freight_rate: Optional[float] = Field(
        default=0.0,
        description="Rate used for freight calculations (per unit for Freight Rate, per day for Daily Rate)."
    )
    cargo_broker: Optional[List["BrokerDetailSchema"]] = Field(
        default_factory=list,
        description="List of brokers involved in the cargo transaction with their commission details."
    )
    daily_rate: Optional[float] = Field(
        default=0.0,
        description="Daily rate for cargo."
    )
    is_cp_terms_updated: Optional[bool] = False

    @field_validator("freight_type", "bill_by", mode="before")
    @classmethod
    def validate_freight_type(cls, value, info):
        if info.field_name == "freight_type":
            if not value:
                return "Frt Rate"
            if isinstance(value, str):
                return FreightTypeEnum(value)
        if info.field_name == "bill_by":
            if not value:
                return None
            if isinstance(value, str):
                return BillQuantityTypeEnum(value)
        return value


class BrokerDetailSchema(BaseModel):
    rate: Optional[float] = 0.0
    lumpsum: Optional[float] = 0.0
    type: Optional[BrokerDetailAmountTypeEnum] = None
    beneficiary: Optional[int] = None
    freight_commission: Optional[FreightCommissionOptionEnum] = None
    demurrage_commission: Optional[DemurrageCommissionEnum] = None
    beneficiary_name: Optional[str] = None

    @field_validator("type", "freight_commission", "demurrage_commission", mode="before")
    @classmethod
    def validate_amount_type(cls, value):
        if not value:
            return None
        return value


class CargoBrokerSchema(BaseModel):
    cargo_sequence: Optional[int] = 1
    broker_details: Optional[List[BrokerDetailSchema]] = []


class CollapsedViewCalculation(BaseModel):
    is_substractable: Optional[bool] = None
    name: Optional[str] = None
    value: Optional[float] = 0.0


class Expenses(BaseModel):
    is_substractable: Optional[bool] = None
    name: Optional[str] = None
    value: Optional[float] = 0.0


class PortItineraryBunkerSchema(BaseModel):
    fuel_type: str
    port_consumption: Optional[float] = 0.0
    rob_arrival: Optional[float] = 0.0
    rob_departure: Optional[float] = 0.0
    received_quantity: Optional[float] = 0.0
    sea_consumption: Optional[float] = 0.0
    price: Optional[float] = 0.0
    is_arrival_updated: Optional[bool] = False
    is_departure_updated: Optional[bool] = False
    bunker_lifting: Optional["BunkeringBillingSchema"] = None


class BunkeringBillingSchema(BaseModel):
    vendor: Optional[int] = None
    vendor_name: Optional[str] = None
    purpose: Optional[str] = None
    delivery_date: Optional[datetime] = None
    lifting_status: Optional[str] = None
    bill_id: Optional[str] = None
    bill_number: Optional[str] = None
    bill_status: Optional[str] = None
    bunker_id: Optional[str] = None


class BasePortItinerarySchema(BaseModel):
    """
    Base schema containing common fields for port itinerary
    """
    american_petroleum_institute_value: Optional[float] = None
    specific_gravity: Optional[float] = None
    avg_speed_of_leg: float
    base_expense: Optional[float] = 0.0
    berth: Optional[str] = None
    bunkers: Optional[List[PortItineraryBunkerSchema]] = []
    cargo: Optional[str] = None
    cargo_volume: Optional[float] = 0.0
    co2_factor: Optional[float] = 0.0
    demurrage_despatch_amount: Optional[float] = 0.0
    demurrage_despatch_days: Optional[float] = 0.0
    demurrage_rate_per_day: Optional[float] = 0.0
    despatch_rate_per_day: Optional[float] = 0.0
    distance_from_previous_port: float = Field(..., description="Distance from previous port in nautical miles")
    draft: Optional[float] = 0.0
    draft_unit: Optional[str] = None
    eca_miles: Optional[float] = 0.0
    eta_day: Optional[str] = None
    etd_day: Optional[str] = None
    extra_port_days: Optional[float] = 0.0
    is_estimate_time_arrival_updated: Optional[bool] = False
    is_estimate_time_departure_updated: Optional[bool] = False
    is_no_of_sea_days_updated: Optional[bool] = False
    is_no_of_extra_sea_days_updated: Optional[bool] = False
    is_port_days_updated: Optional[bool] = None
    lat: Optional[str] = None
    load_discharge_quantity: Optional[float] = Field(..., description="Load or discharge quantity")
    load_discharge_rate: Optional[float] = Field(..., description="Load or discharge rate")
    load_discharge_rate_unit: Optional[str] = "Per Day"
    load_line: Optional[str] = None
    lon: Optional[str] = None
    eca_port_days: Optional[float] = 0.0
    eca_sea_days: Optional[float] = 0.0
    max_lift_quantity: Optional[float] = 0.0
    name: Optional[str] = None
    no_of_extra_sea_days: Optional[float] = 0.0
    no_of_sea_days: Optional[float] = 0.0
    nor_hours: Optional[float] = 0.0
    port: Optional[str] = Field(..., description="Port unique ID")
    port_days: Optional[float] = 0.0
    port_expenses: Optional[float] = 0.0
    port_expenses_currency: Optional[str] = None
    port_expenses_in_dollar_per_ton: Optional[float] = 0.0
    port_function: Optional[PortFunctionEnum] = Field(..., description="The current port function")
    port_name: Optional[str] = None
    rob_arrival: Optional[float] = 0.0
    salinity: Optional[float] = 0.0
    sequence_no: int
    stowage_factor_cubicmeters_mt: Optional[float] = 0.0
    stowage_factor_cubicfeet_mt: Optional[float] = 0.0
    terms: Optional[str] = None
    time_zone: Optional[float] = 0.0
    total_port_days: Optional[float] = 0.0
    sea_days: Optional[float] = 0.0
    total_sea_days: Optional[float] = 0.0
    use_cranes: Optional[bool] = None
    weather_factor_percent: Optional[float] = 0.0
    ballast_or_laden: Optional[str] = None
    eca_zone: Optional[bool] = False
    estimate_time_arrival: Optional[str] = Field(...,
                                                 description="Estimated time of arrival at the port in format YYYY-MM-DD")
    estimate_time_departure: Optional[str] = Field(...,
                                                   description="Estimated time of departure from the port in format YYYY-MM-DD")
    bunker_expense: Optional[float] = 0.0


class PortItineraryInputSchema(BasePortItinerarySchema):
    """
    Input schema with datetime fields for timestamps
    """
    is_port_expense_updated: Optional[bool] = False


class PortItineraryOutputSchema(BasePortItinerarySchema):
    """
    Output schema with string fields for timestamps
    """
    pass


class Co2PricePerMT(BaseModel):
    currency: str
    value: float


class EmissionItem(BaseModel):
    is_port_ets_emission_changed: bool
    is_sea_ets_emission_changed: bool
    phase_in_percentage: float
    port_emission: float
    port_ets_emission: float
    port_ets_percentage: float
    port_function: Optional[PortFunctionEnum] = Field(..., description="The current port function")
    port_name: str
    sea_emission: float
    sea_ets_emission: float
    sea_ets_percentage: float
    total_emission: float
    total_ets_emission: float
    total_eu_ets_exp: float


class CarbonSchema(BaseModel):
    cost: Optional[dict[str, Any]] = Field(default=None)
    emission: List[dict] = Field(default_factory=list)
    total_ets_cost: float = Field(default=0.0)
    total_ets_cost_usd: float = Field(default=0.0)
    process: bool = Field(default=False)

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

    @field_validator('cost', mode='before')
    @classmethod
    def validate_cost(cls, value):
        if isinstance(value, dict):
            return value
        if isinstance(value, Cost):
            return {
                'co2_price_per_MT': {
                    'currency': value.co2_price_per_MT.currency,
                    'value': value.co2_price_per_MT.value
                },
                'exchange_rate': {
                    'currency': value.exchange_rate.currency,
                    'value': value.exchange_rate.value
                }
            }
        return value


class RevenueExpenseDetail(BaseModel):
    amount: float
    amount_in_base_currency: str
    currency: str
    description: str
    exchange_rate: str
    is_expenses: str
    is_non_accounting_invoice: str
    is_port_expenses: str
    name: str
    type: str


class TimeCharterHireSchema(BaseModel):
    hire_duration: float
    hire_duration_type: str
    hire_rate: float
    hire_rate_type: str


class TimeCharterTerms(BaseModel):
    address_commission: float
    ballast_bonus: float
    ballast_bonus_commissionble: bool
    broker_commission: float
    broker_terms: str
    delivery_port: str
    delivery_port_latitude: float
    delivery_port_longitude: float
    delivery_port_name: str
    redelivery_port: str
    redelivery_port_latitude: float
    redelivery_port_longitude: float
    redelivery_port_name: str
    tab_hire: str
    charter: str


class DelayDates(BaseModel):
    activity: str
    reason: str
    delay_starts: str
    delay_ends: str
    add_zone: float
    ded_adj: float
    deduct_zone: float
    delay_hours: float
    include_PnL: bool
    hsf_qty: float
    lsf_qty: float
    mgo_qty: float
    lsg_qty: float
    ulf_qty: float
    vlsfo_qty: float
    ov_percentage: float
    tci_percentage: float
    tco_percentage: float
    ov_daily_cost: float
    tci_daily_cost: float
    tco_daily_cost: float
    tco_l: bool
    tci_l: bool
    tci_lumpsum: float
    tco_lumpsum: float
    remarks: str
    last_updated: str
    last_updated_by: str


class FuelConsumptionDetailSchema(BaseModel):
    fuel_type: str
    fuel_grade: str
    loading_consumptions: float
    discharge_consumption: float
    idle_consumptions: float
    speed_ballast_consumption: float
    speed_laden_consumption: float


class FuelConsumptionDataSchema(BaseModel):
    fuel_consumption_entries: List[FuelConsumptionDetailSchema]


class EstimateAIRequestBody(BaseModel):
    company_id: str = Field(description="ID of the company")
    daily_addcom: Optional[int] = Field(0, description="Daily additional commission")
    daily_cost: int = Field(description="Daily cost")
    vessel_id: UUID = Field(description="ID of the vessel")
    vessel_dwt: int = Field(description="Deadweight tonnage of the vessel")
    weather_factor: float = Field(description="Weather factor")
    cargo_name: str = Field(description="Name of the cargo")
    cargo_quantity: float = Field(description="Quantity of the charter party cargo")
    cargo_unit: str = Field(description="Unit of the charter party cargo")
    freight_rate: float = Field(description="Freight rate")
    freight_type: str = Field(description="Type of freight")
    estimate_sheet_id: str = Field(description="ID of the estimate sheet")
    commencing_date: str = Field(default=str(datetime.now() + timedelta(days=10)), description="Commencing date")
    load_port_id: UUID = Field(description="ID of the load port")
    discharge_port_id: UUID = Field(description="ID of the discharge port")
    cargo_id: UUID = Field(description="ID of the cargo")
    contact_id: str = Field(description="ID of the contact")
    is_own_voyage: bool = Field(description="Indicates if it is voyage charter out")
    is_time_chaterer_voyage: bool = Field(description="Indicates if it is time charterer voyage")
    cargo_additional_commission_in_percentage: Optional[float] = Field(None,
                                                                       description="Additional commission percentage for cargo")
    load_rate: Optional[float] = Field(None, description="Load rate")
    load_port_terms: Optional[str] = Field(None, description="Terms of the load port")
    load_rate_unit: Optional[str] = Field(None, description="Unit of the load rate")
    load_port_expense_in_usd: Optional[float] = Field(None, description="Expense of the load port in USD")
    discharge_rate: Optional[float] = Field(None, description="Discharge rate")
    discharge_port_terms: Optional[str] = Field(None, description="Terms of the discharge port")
    discharge_rate_unit: Optional[str] = Field(None, description="Unit of the discharge rate")
    discharge_port_expense_in_usd: Optional[float] = Field(None, description="Expense of the discharge port in USD")
    bunker: Optional[Union[str, List[dict]]] = Field(None, description="Bunker information")
    broker_commission_in_percentage: Optional[float] = Field(None, description="Broker commission percentage")
    cargo_option_percentage: Optional[float] = Field(None, description="Cargo option percentage")
    commencing_port_id: Optional[UUID] = Field(None, description="ID of the commencing port")
    laden_speed: Optional[float] = Field(None, description="Laden speed")
    ballast_speed: Optional[float] = Field(None, description="Ballast speed")
    vessel_additional_commission_in_percentage: Optional[float] = Field(None,
                                                                        description="Additional commission percentage for vessel")
    number: Optional[int] = Field(None, description="Number")
    estimate_id: Optional[str] = Field(None, description="ID of the estimate")


class CargoBookMappingEstimate(BaseModel):
    cargo_book_id: str = ""


class UserChangedCarbonSchema(BaseModel):
    cost: Optional[dict[str, Any]] = Field(default=None)
    emission: Optional[list] = None
    total_ets_cost: Optional[float] = None
    total_ets_cost_usd: Optional[float] = None
    process: Optional[bool] = None


class DwtDraft(BaseModel):
    """Schema for DWT-Draft relationship"""
    dwt: Optional[float] = 0
    draft: Optional[float] = 0


class VesselDetails(BaseModel):
    """Schema for vessel details"""
    dwt: Optional[float] = 0
    summer_draft: Optional[float] = 0
    winter_dwt: Optional[float] = 0
    winter_draft: Optional[float] = 0
    tropical_sw_draft: Optional[float] = 0
    tropical_sw_dwt: Optional[float] = 0
    tpc: Optional[float] = 0
    bale: Optional[float] = 0
    grain: Optional[float] = 0
    type_code: Optional[str] = "Bulk Carrier"
    constants_sea: Optional[float] = 0
    fresh_water: Optional[float] = 0
    others: Optional[float] = 0
    daily_cost: Optional[float] = 0
    ownership: Optional[str] = "OV - Owned Vessel"
    dwt_lightship: Optional[float] = 0
    draft_lightship: Optional[float] = 0
    is_vessel_updated: Optional[bool] = False
    dwt_draft: Optional[List[DwtDraft]] = []


class TimeCharterBallastBonusDetail(BaseModel):
    rate: Optional[float] = 0.0
    terms: Optional[Literal["Deduct from invoice"]] = None

    @field_validator("terms", mode="before")
    @classmethod
    def validate(cls, value: Any):
        if not value:
            return None
        return value


class EstimateRequestSchema(BaseModel):
    tc_out_ballast_bonus: Optional[TimeCharterBallastBonusDetail] = TimeCharterBallastBonusDetail()
    tc_in_ballast_bonus: Optional[TimeCharterBallastBonusDetail] = TimeCharterBallastBonusDetail()
    vessel_details: Optional[VesselDetails] = Field(...,
                                                    description="Vessel details get from get_vessel_details tool with ")
    annual_distance_sailed: Optional[float] = 0.0
    avoid_piracy: Optional[bool] = True
    ballast_bonus: Optional[float] = 0.0
    ballast_speed: float
    is_ballast_speed_updated: Optional[bool] = False
    is_laden_speed_updated: Optional[bool] = False
    is_port_days_updated: Optional[bool] = None
    tco_hire_rate_column_view: Optional[float] = 0.0
    broker: Optional[List[Broker]] = []
    bunker_fuel_calculation: Optional[bool] = None
    bunker_planning: Optional[List[BunkerPlanningSchema]] = []
    eca: Optional[List[EmissionZoneSchema]] = Field(...,
                                                    description="Emission Control Area get bunker info from vessel details")
    non_eca: Optional[List[EmissionZoneSchema]] = Field(...,
                                                        description="Non Emission Control Area get bunker info from vessel details")
    carbon: Optional[CarbonSchema] = None
    user_changed_carbon: dict = {}
    cargo: List[CargoData]
    category: Optional[str] = ""
    charter_specialist: Optional[str] = None
    collapsed_view_calculation: Optional[List[CollapsedViewCalculation]] = None
    commencing_date: Optional[str] = Field(..., description="Commencing date in format YYYY-MM-DD")
    completion_date: Optional[str] = Field(..., description="Completion date in format YYYY-MM-DD")
    daily_addcom: float
    daily_cost: float
    estimate_created_by_id: Optional[str] = None
    estimate_id: str = Field(..., description="Estimate sheet unique ID")
    estimate_sheet_is_public: bool
    estimate_sheet_name: str
    expense: Optional[List['ExpensesData']] = None
    is_created: Optional[bool] = False
    laden_speed: float
    misc_income: Optional[float] = 0
    misc_expense: Optional[float] = 0
    name: str
    sequence_no: Optional[int] = None
    operation_type: str
    port_itinerary: List[PortItineraryInputSchema]
    profit_loss: Optional[List['ProfitLossData']] = None
    remarks: str = ""
    revenue: Optional[List['RevenueData']] = None
    revenue_and_expense: List
    running_cost: Optional[List['RunningCost']] = None
    sea_consumption_aps: Optional[float] = 0.0
    sea_days_aps: Optional[float] = 0.0
    time_charter_hire: Optional[List[TimeCharterHireSchema]] = []
    total_bunker_expense: Optional[float] = 0.0
    total_port_days: Optional[float] = 0.0
    total_sea_days: Optional[float] = 0.0
    trade_area: Optional[str] = ""
    use_scrubber: Optional[bool] = False
    vessel: Optional[str] = Field(..., description="Vessel unique ID")
    vessel_dwt: Optional[float] = 0.0
    voyage_days: Optional[float] = 0.0
    weather_factor: Optional[int] = 5
    delay_dates: Optional[list[DelayDatesSchema]] = []
    delay_bunkers: Optional[List['DelayBunkerEntries']] = []
    cargo_book_estimates: Optional[List[CargoBookMappingEstimate]] = []
    validator: dict = Field(default_factory=lambda: {"error": [], "warnings": []})
    cargo_broker: Optional[CargoBrokerSchema]
    cp_terms: Optional[CpTerms] = None
    model_config = ConfigDict(
        from_attributes=True
    )
    other_revenue: Optional[List["OtherRevenueSchema"]] = []
    other_expense: Optional[List["OtherExpenseSchema"]] = []
    port_expense: Optional[List["PortExpenseSchema"]] = []
    port_expense_delete_sequence: Optional[int] = None
    tco_cve: Optional[List["TcoCveModelSchema"]] = []
    tci_cve: Optional[List["TciCveModelSchema"]] = []
    seca_enabled: Optional[bool] = False


class EstimateAIRequestBodyResponse(BaseModel):
    message: str
    request_data: Optional[EstimateAIRequestBody] = None
    estimate_id: Optional[UUID] = None
    estimate_sheet_id: Optional[UUID] = None
    cargo_id: Optional[UUID] = None
    calculated_data: Optional[dict] = None
    estimate_sheet_name: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "message": "Estimate Created Successfully",
                "request_data": {},
                "estimate_id": "123e4567-e89b-12d3-a456-426614174000",
                "estimate_sheet_id": "123e4567-e89b-12d3-a456-426614174001",
                "cargo_id": "123e4567-e89b-12d3-a456-426614174002"
            }
        }


class PnLData(BaseModel):
    is_substractable: Optional[bool] = None
    name: Optional[str] = None
    value: Optional[float] = 0.0


class ProfitLossData(PnLData):
    pass


class RevenueData(PnLData):
    pass


class ExpensesData(PnLData):
    pass


class RunningCost(PnLData):
    pass


class RevenueAndExpense(BaseModel):
    amount: Optional[float] = 0.0
    amount_in_base_currency: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[str] = None
    is_expenses: Optional[str] = None
    is_non_accounting_invoice: Optional[str] = None
    is_port_expenses: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class DelayBunkerConsumption(BaseModel):
    fuel_type: Optional[str] = None
    quantity: Optional[float] = 0.0
    price: Optional[float] = 0.0
    tco_price: Optional[float] = 0.0


class DelayBunkerEntries(BaseModel):
    activity: Optional[str] = None
    reason: Optional[str] = None
    bunker_consumption: Optional[List[DelayBunkerConsumption]] = None
    # delay_starts: Optional[str] = None
    # delay_ends: Optional[str] = None
    include_PnL: Optional[bool] = None


class CargoBookIds(BaseModel):
    cargo_book_id: Optional[str] = None


class TimeCharterTermsSchema(BaseModel):
    address_commission: Optional[float] = 0.0
    ballast_bonus: Optional[float] = 0.0
    ballast_bonus_commissionble: Optional[bool] = False
    broker_commission: Optional[float] = 0.0
    broker_terms: Optional[str] = None
    delivery_port: Optional[str] = None
    delivery_port_latitude: Optional[float] = 0.0
    delivery_port_longitude: Optional[float] = 0.0
    delivery_port_name: Optional[str] = None
    redelivery_port: Optional[str] = None
    redelivery_port_latitude: Optional[float] = 0.0
    redelivery_port_longitude: Optional[float] = 0.0
    redelivery_port_name: Optional[str] = None
    tab_hire: Optional[str] = None
    charter: Optional[str] = None


class TotalPortItinerarySchema(BaseModel):
    co2_factor: float = 0.0
    port_expenses: float = 0.0
    no_of_sea_days: float = 0.0
    port_days: float = 0.0
    total_port_days: float = 0.0
    eca_miles: float = 0.0
    distance_from_previous_port: float = 0.0
    no_of_extra_sea_days: float = 0.0


class EstimateResponse(BaseModel):
    # vessel details
    tc_out_ballast_bonus: Optional[TimeCharterBallastBonusDetail] = TimeCharterBallastBonusDetail()
    tc_in_ballast_bonus: Optional[TimeCharterBallastBonusDetail] = TimeCharterBallastBonusDetail()
    vessel: Optional[str] = None
    vessel_details: Optional[VesselDetails]
    ballast_speed: Optional[float] = 0.0
    is_ballast_speed_updated: Optional[bool] = False
    is_laden_speed_updated: Optional[bool] = False
    ballast_bonus: Optional[float] = 0.0
    daily_addcom: Optional[float] = 0.0
    daily_cost: Optional[float] = None
    laden_speed: Optional[float] = 0.0
    vessel_dwt: Optional[float] = 0.0

    # estimate details 
    commencing_date: Optional[str] = Field(..., description="Commencing date")
    completion_date: Optional[datetime] = Field(..., description="Completion date")
    annual_distance_sailed: Optional[float] = 0.0
    remarks: Optional[str] = None
    user_changed_carbon: Optional[UserChangedCarbonSchema] = None
    carbon: Optional[CarbonSchema] = None
    charter_specialist: Optional[str] = None
    name: Optional[str] = None
    sequence_no: Optional[int] = 1
    operation_type: Optional[str] = None
    revenue_and_expense: Optional[List[RevenueAndExpense]] = None
    trade_area: Optional[str] = None
    port_itinerary: Optional[List[PortItineraryOutputSchema]] = None
    use_scrubber: Optional[bool] = False

    # Other revenue, Other expense, Port expense, TCO CVE and TCI CVE
    other_revenue: Optional[List["OtherRevenueSchema"]] = []
    other_expense: Optional[List["OtherExpenseSchema"]] = []
    port_expense: Optional[List["PortExpenseSchema"]] = []
    tco_cve: Optional[List["TcoCveModelSchema"]] = []
    tci_cve: Optional[List["TciCveModelSchema"]] = []

    # Bunker Details
    bunker_planning: Optional[List[BunkerPlanningSchema]] = []
    eca: Optional[list[EmissionZoneSchema]] = []
    non_eca: Optional[List[EmissionZoneSchema]] = []

    # TCOUT
    broker: Optional[List[Broker]] = None
    cargo: Optional[List[CargoData]] = None
    time_charter_hire: Optional[List[TimeCharterHireSchema]] = []

    # ROUTING details
    seca_enabled: Optional[bool] = True
    avoid_piracy: Optional[bool] = True

    # extras
    is_port_days_updated: Optional[bool] = None
    tco_hire_rate_column_view: Optional[float] = 0.0
    bunker_fuel_calculation: Optional[bool] = None
    collapsed_view_calculation: Optional[List[CollapsedViewCalculation]] = None
    is_created: Optional[bool] = False

    # Meta data
    company: Optional[str] = None
    company_id: Optional[str] = None
    estimate_created_by_id: Optional[str] = None
    estimate_id: Optional[str] = None
    cargo_book_estimates: Optional[List[CargoBookMappingEstimate]] = []

    # Estimate Sheet details
    estimate_sheet_is_public: Optional[bool] = None
    estimate_sheet_name: Optional[str] = None

    # Profit Loss
    expense: Optional[List[ExpensesData]] = []
    profit_loss: Optional[List[ProfitLossData]] = []
    revenue: Optional[List[RevenueData]] = []
    running_cost: Optional[List[RunningCost]] = []

    # OFFHIRE Details
    delay_dates: Optional[list[DelayDatesSchema]] = []
    delay_bunkers: Optional[List[DelayBunkerEntries]] = None

    # MISC DATA
    total_port_days: Optional[float] = 0.0
    total_sea_days: Optional[float] = 0.0
    voyage_days: Optional[float] = 0.0
    weather_factor: Optional[float] = 0.0

    port_expense_delete_sequence: Optional[int] = None
    validator: dict = {}
    total_port_itinerary: Optional[TotalPortItinerarySchema] = None

    # CONFIG
    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            datetime: lambda dt: dt.strftime("%d %b %Y | %H:%M") if dt else None
        }
    )

    @field_validator('port_itinerary', mode='before')
    @classmethod
    def validate_port_itinerary(cls, value):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for field in ['estimate_time_arrival', 'estimate_time_departure']:
                        if isinstance(item.get(field), datetime):
                            item[field] = str(item[field])
        return value

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )


class CreateEstimateResponse(BaseModel):
    data: Optional[str] = None
    worksheet_id: Optional[str] = None


class EstimateVoyageInput(BaseModel):
    estimate_sheet_id: Optional[str] = None


class EstimateDeletableResponse(BaseModel):
    estimate_id: Optional[str] = None
    is_deletable: Optional[bool] = None


class EstimateVoyageOutput(BaseModel):
    error_flag: Optional[str] = None
    message: Optional[str] = None
    data: Optional[List[EstimateDeletableResponse]]


class EstimateSheetInput(BaseModel):
    company_id: Optional[str] = None


class EstimateSheetResponse(BaseModel):
    estimate_count: Optional[str] = None
    last_updated: Optional[str] = None
    entry_date: Optional[str] = None
    last_user: Optional[str] = None
    worksheet_name: Optional[str] = None
    worksheet_type: Optional[str] = None
    id: Optional[str] = None
    voyage_count: Optional[str] = None


class EstimateSheetList(BaseModel):
    error_flag: Optional[str] = None
    message: Optional[str] = None
    data: Optional[List[EstimateData]]


class EstimateList(BaseModel):
    error_flag: Optional[str] = None
    message: Optional[str] = None


class EstimateOffhireOutput(BaseModel):
    data: Optional[EstimateOffHireSchema]
    error_flag: Optional[str] = None
    message: Optional[str] = None


class EstimateOffhireInput(BaseModel):
    estimate_id: Optional[str] = None
    vessel_id: Optional[str] = None


class EstimateSheetOutputResponse(BaseModel):
    error_flag: Optional[str] = None
    message: Optional[str] = None
    estimate_sheet_id: Optional[UUID] = None


class BunkerPlanningItem(BaseModel):
    calculation_method: Optional[str] = None
    fuel_type: Optional[str] = None
    fuel_grade: Optional[str] = None
    price: Optional[float] = 0.0
    initial_price: Optional[float] = 0.0
    initial_quantity: Optional[float] = 0.0
    consumption_rate_at_ballast_speed: Optional[float] = 0.0
    consumption_rate_at_laden_speed: Optional[float] = 0.0
    consumption_rate_at_daily_discharging: Optional[float] = 0.0
    consumption_rate_at_idle_speed: Optional[float] = 0.0
    consumption_rate_at_loading: Optional[float] = 0.0


class ExpensesBaseModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    port_name: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    exchange_rate: Optional[float] = None
    amount_in_base_currency: Optional[float] = None


class RevenueExpenseBase(ExpensesBaseModel):
    cargo_no: Optional[int] = None
    port_sequence_no: Optional[int] = None
    payment_type: Optional[PaymentTypeEnum] = "Lumpsum"
    is_non_accounting_invoice: Optional[bool] = False
    cargo_name: Optional[str] = None
    operation_ledger: Optional[UUID] = None

    @field_validator('payment_type', mode='before')
    @classmethod
    def validate_payment_type(cls, value):
        if not value:
            return None
        return value


class OtherRevenueSchema(RevenueExpenseBase):
    pass

    @field_validator('operation_ledger', 'payment_type', mode='before')
    @classmethod
    def validate_port_itinerary(cls, value):
        if not value:
            return None
        return value


class OtherExpenseSchema(RevenueExpenseBase):
    rebillable_category: Optional[RebillableCategoryChoicesEnum] = "Non-Rebillable"

    @field_validator('operation_ledger', 'payment_type', mode='before')
    @classmethod
    def validate_port_itinerary(cls, value):
        if not value:
            return None
        return value


class PortExpenseSchema(ExpensesBaseModel):
    port_sequence_no: Optional[int] = None
    port_function: Optional[PortFunctionEnum] = Field(..., description="The current port function")
    ledger_expense: Optional[UUID] = None
    rebillable_category: Optional[RebillableCategoryChoicesEnum] = "Non-Rebillable"

    @field_validator('ledger_expense', 'rebillable_category', mode='before')
    @classmethod
    def validate_port_itinerary(cls, value):
        if not value:
            return None
        return value


class BaseCveModel(BaseModel):
    cve_code_id: Optional[int] = None
    code: Optional[CveCodeEnum] = None
    description: Optional[str] = None
    rate_type: Optional[CVERateTypeEnum] = "Monthly"
    amount: Optional[float] = 0
    remarks: Optional[str] = None

    @field_validator("rate_type", mode='before')
    @classmethod
    def validate_request(cls, value):
        if not value:
            return "Monthly"
        return value


class TcoCveModelSchema(BaseCveModel):
    pass


class TciCveModelSchema(BaseCveModel):
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None


class VoyageProfitAndLoss(BaseModel):
    end_date: Optional[str] = Field(..., description="Voyage end date format YYYY-MM-DD")
    project_id: Optional[str] = Field(..., description="Voyage project id get from voyage details")
    start_date: Optional[str] = Field(..., description="Voyage start date format YYYY-MM-DD")
    voyage_id: Optional[str] = Field(..., description="Voyage id")


class BillQueryParams(BaseModel):
    """Parameters for querying bills with proper field descriptions and default values"""
    
    status: Optional[str] = Field(
        None, 
        description="Status of the bills to filter by"
    )
    page: str = Field(
        default="1",
        description="Page number for pagination",
        alias="page"
    )
    per_page: str = Field(
        default="20",
        description="Number of records per page",
        alias="per_page"
    )
    project_id: Optional[str] = Field(
        None,
        description="ID of the project to filter bills by"
    )
    number: Optional[str] = Field(
        None,
        description="Bill number to filter by"
    )
    vendor_name: Optional[str] = Field(
        None,
        description="Vendor name to filter bills by"
    )
    client_status: Optional[str] = Field(
        None,
        description="Client status to filter by"
    )
    search_key: Optional[str] = Field(
        None,
        description="Search keyword for filtering bills"
    )
    field_name: str = Field(
        default="",
        description="Column name to sort the bills by",
        alias="field_name"
    )
    order: str = Field(
        default="",
        description="Sort order ('asc' or 'desc')",
        alias="order"
    )
    expense_status: Optional[str] = Field(
        None,
        description="Expense status to filter bills by"
    )
    sort: Optional[str] = Field(
        None,
        description="Sorting method to apply"
    )
    vendor_id: Optional[str] = Field(
        None,
        description="Vendor ID to filter bills by"
    )
    type: Optional[str] = Field(
        None,
        description="Type of bills to filter by"
    )

    class Config:
        """Pydantic model configuration"""
        json_schema_extra = {
            "example": {
                "status": "active",
                "page": "1",
                "per_page": "20",
                "field_name": "created_at",
                "order": "desc"
            }
        }


class ListInvoiceParams(BaseModel):
    client_status: Optional[str] = None
    project_id: Optional[str] = None
    status_id: Optional[str] = None
    status: Optional[str] = None
    client_id: Optional[str] = None
    sort: Optional[str] = None
    page: Optional[str] = Field("", alias="page")
    per_page: Optional[str] = Field("", alias="per_page")
    filter: Optional[str] = None
    field_name: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None