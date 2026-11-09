# applied-control

Papers, engineering blogs, technical reports, and talks on control systems that left the lab: how organizations model, estimate, optimize, tune, and verify feedback that runs on rockets, cars, robots, plants, grids, patients, and production software.

**248 deployment case studies** from **251 organizations** across **7 domains** (1967–2025), plus **41** surveys, tools, talks, and books. Browse the [interactive explorer](https://das-goutam.github.io/applied-control/), or the indexes [by method](docs/by-method.md) and [by organization](docs/by-organization.md).

Control theory runs much of the modern world, but the evidence of how it is used in practice is
scattered across flight-test reports, industrial journals, clinical trials, and company
engineering blogs. Inspired by [applied-ml](https://github.com/eugeneyan/applied-ml), this list
collects that evidence in one place, organized by application domain.

**What qualifies.** Every case-study entry documents a controller that actually ran outside the
lab, in a shipped product, on a flight vehicle, in patients, in an operating plant, or in
production software, and explains how it works. Simulation-only studies are out of scope. The
final section collects cross-cutting resources: industry surveys, open-source software with
documented deployments, practitioner talks, and books.

**How to read an entry**

Each entry gives the title, the organizations behind the deployment, the year, and the format, followed by a one-line summary. The small print shows the deployment stage and the control methods involved.

| Stage | Meaning | Entries |
|---|---|---|
| `production` | Shipped in a commercial product or running in production software | 88 |
| `flight` | Flown on an aircraft, spacecraft, or launch vehicle | 25 |
| `clinical` | Used in human clinical trials or an approved medical device | 32 |
| `field` | Tested on real hardware or infrastructure outside the lab, not yet a product | 80 |
| `operations` | Running in an operating plant, grid, fleet, or facility (also used for surveys and books) | 23 |

## Contents

- **[Aerospace & Space](#aerospace--space)** (36)  
  [Launch & landing](#launch--landing) · [Planetary EDL & landers](#planetary-edl--landers) · [Spacecraft attitude & orbit control](#spacecraft-attitude--orbit-control) · [Aircraft flight control](#aircraft-flight-control) · [UAVs & drones](#uavs--drones) · [Air traffic & collision avoidance](#air-traffic--collision-avoidance)
- **[Automotive, Rail & Maritime](#automotive-rail--maritime)** (41)  
  [Powertrain & energy management](#powertrain--energy-management) · [Vehicle dynamics & chassis](#vehicle-dynamics--chassis) · [ADAS & autonomous driving](#adas--autonomous-driving) · [Traffic & mobility](#traffic--mobility) · [Rail](#rail) · [Maritime](#maritime)
- **[Robotics](#robotics)** (35)  
  [Legged locomotion](#legged-locomotion) · [Humanoids & whole-body control](#humanoids--whole-body-control) · [Manipulation & industrial arms](#manipulation--industrial-arms) · [Mobile, warehouse & field robots](#mobile-warehouse--field-robots) · [Aerial robotics](#aerial-robotics) · [Surgical robots](#surgical-robots) · [Entertainment robots](#entertainment-robots) · [Space & underwater robots](#space--underwater-robots)
- **[Process Industries & Manufacturing](#process-industries--manufacturing)** (28)  
  [Refining & chemicals](#refining--chemicals) · [Pulp & paper](#pulp--paper) · [Metals, mining & cement](#metals-mining--cement) · [Pharmaceuticals](#pharmaceuticals) · [Semiconductors & precision motion](#semiconductors--precision-motion) · [Oil & gas production](#oil--gas-production)
- **[Energy, Buildings & Infrastructure](#energy-buildings--infrastructure)** (37)  
  [Power grids & storage](#power-grids--storage) · [Wind & solar](#wind--solar) · [Data centers](#data-centers) · [Buildings & HVAC](#buildings--hvac) · [Nuclear & fusion](#nuclear--fusion) · [Water & wastewater](#water--wastewater)
- **[Computing, Networks & Marketplaces](#computing-networks--marketplaces)** (36)  
  [Congestion control & networking](#congestion-control--networking) · [Video streaming & adaptive bitrate](#video-streaming--adaptive-bitrate) · [Autoscaling & resource management](#autoscaling--resource-management) · [Load shedding & overload control](#load-shedding--overload-control) · [Ads, marketplaces & inventory](#ads-marketplaces--inventory)
- **[Healthcare & Agriculture](#healthcare--agriculture)** (35)  
  [Glucose control & insulin delivery](#glucose-control--insulin-delivery) · [Anesthesia & critical care](#anesthesia--critical-care) · [Neuromodulation & cardiac devices](#neuromodulation--cardiac-devices) · [Prosthetics & rehabilitation](#prosthetics--rehabilitation) · [Agriculture](#agriculture)
- **[Resources](#resources)** (41)  
  [Industry surveys & impact reports](#industry-surveys--impact-reports) · [Software with documented deployments](#software-with-documented-deployments) · [Talks & videos](#talks--videos) · [Books & long-form guides](#books--long-form-guides)
- [Browse by method](#browse-by-method)
- [Related lists](#related-lists)
- [Contributing](#contributing)

## Aerospace & Space

Guidance, navigation, and control for launch vehicles, landers, spacecraft, aircraft, drones, and airspace safety.

### Launch & landing

1. **[Path to First Flight of Adaptive Augmenting Control on NASA's Space Launch System for Artemis I](https://airdrive.eventsair.com/eventsairwesteuprod/production-atpi-public/f897c45dbb804d90bb069fda35739183)** · NASA MSFC, NASA NESC · 2023 · *paper*  
   Traces NASA's adaptive augmenting controller, a multiplicative gain adjustment atop the SLS baseline autopilot, from concept to the Artemis I launch, where it behaved within preflight predictions. <sub>`flight` · adaptive control · gain scheduling</sub>
2. **[Post-Flight Performance Analysis of Navigation and Advanced Guidance Algorithms on a Terrestrial Suborbital Rocket Flight](https://ntrs.nasa.gov/citations/20210023718)** · NASA, Draper, Blue Origin · 2022 · *paper*  
   NASA, Draper and Blue Origin assess SPLICE terrain-relative navigation and successive-convexification powered-descent guidance that ran onboard New Shepard in open loop, converging within three seconds. <sub>`flight` · Kalman filtering · convex optimization · trajectory optimization</sub>
3. **[Autonomous Precision Landing of Space Rockets](https://www.nationalacademies.org/read/23659/chapter/10)** · SpaceX · 2017 · *paper*  
   SpaceX's principal landing engineer explains Falcon 9 booster landing guidance, which solves a convex trajectory problem onboard in real time using CVXGEN-generated flight code. <sub>`flight` · convex optimization · trajectory optimization</sub>
4. **[Customized Real-Time Interior-Point Methods for Onboard Powered-Descent Guidance](https://doi.org/10.2514/1.G001480)** · University of Washington, NASA JPL · 2017 · *paper*  
   Generated custom second-order-cone interior-point solvers fast and deterministic enough for flight computers, with this solver family flown onboard Masten's Xombie rocket during 2012-2013 G-FOLD tests. <sub>`flight` · convex optimization</sub>
5. **[Implementation and Experimental Demonstration of Onboard Powered-Descent Guidance](https://doi.org/10.2514/1.G000399)** · NASA JPL, Masten Space Systems · 2017 · *paper*  
   JPL's G-FOLD lossless-convexification divert guidance computed fuel-optimal trajectories for a vertical-takeoff, vertical-landing rocket across eight terrestrial flights, five of them solved onboard. <sub>`flight` · convex optimization · trajectory optimization</sub>
6. **[In-Flight Suppression of a Destabilized F/A-18 Structural Mode Using the Space Launch System Adaptive Augmenting Control System](https://ntrs.nasa.gov/citations/20150002959)** · NASA MSFC, NASA Armstrong · 2015 · *paper*  
   NASA flew the SLS adaptive augmenting controller on an F/A-18 mimicking launch-vehicle dynamics, deliberately destabilizing a structural mode in flight and showing the adaptation suppress it. <sub>`flight` · adaptive control · dynamic inversion</sub>

**[back to top](#contents)**

### Planetary EDL & landers

1. **[Orion Artemis I Entry Performance](https://ntrs.nasa.gov/citations/20240000024)** · NASA JSC · 2024 · *paper*  
   Flight-data assessment of Orion's predictive skip-entry guidance and bank-angle control on Artemis I, which steered the uncrewed capsule through a skip re-entry to its splashdown target. <sub>`flight` · predictor-corrector guidance</sub>
2. **[Flying a Helicopter on Mars: How Ingenuity's Flights were Planned, Executed, and Analyzed](https://doi.org/10.1109/AERO53065.2022.9843813)** · NASA JPL · 2022 · *paper*  
   How JPL planned, flew, and analyzed Ingenuity's autonomous Mars helicopter flights, whose onboard flight control and visual-inertial state estimation operated in thin Martian air. <sub>`flight` · state estimation</sub>
3. **[Mars 2020 Lander Vision System Flight Performance](https://doi.org/10.2514/6.2022-1214)** · NASA JPL · 2022 · *paper*  
   Flight results of Perseverance's Lander Vision System, which matched descent images to an orbital map and fused them with inertial data, enabling hazard-avoiding touchdown about 5 m from target. <sub>`flight` · state estimation</sub>
4. **[Post-Flight EDL Entry Guidance Performance of the 2011 Mars Science Laboratory Mission](https://ntrs.nasa.gov/citations/20130009144)** · NASA JSC, NASA JPL · 2013 · *paper*  
   Post-flight review of Curiosity's Apollo-derived bank-angle entry guidance, the first guided Mars entry, which landed about 2.2 km from target inside a 19 by 7 km ellipse. <sub>`flight` · gain scheduling</sub>
5. **[The Mars exploration rovers descent image motion estimation system](https://doi.org/10.1109/MIS.2004.18)** · NASA JPL · 2004 · *paper*  
   JPL's descent camera system that estimated horizontal velocity from successive images during the 2004 Spirit and Opportunity landings, informing whether to fire transverse rockets before airbag impact. <sub>`flight` · state estimation</sub>
6. **[Apollo lunar descent guidance](https://ntrs.nasa.gov/citations/19740044219)** · Draper Laboratory, NASA · 1974 · *paper*  
   Draper's onboard Lunar Module descent guidance, which steered the Apollo lunar landings by tracking polynomial reference trajectories to terminal targets and let the crew redesignate the landing site. <sub>`flight` · feedforward</sub>

**[back to top](#contents)**

### Spacecraft attitude & orbit control

1. **[JWST Fine Guidance Sensor Commissioning and Performance During Operations](https://ntrs.nasa.gov/citations/20250002384)** · NASA GSFC, STScI, CSA · 2025 · *paper*  
   Commissioning and operations record of JWST's Fine Guidance Sensor, which feeds guide-star measurements to the attitude control loop every 64 ms and sustains roughly 1 milliarcsecond pointing stability. <sub>`operations` · state estimation</sub>
2. **[An Overview of the Artemis I Navigation Performance](https://ntrs.nasa.gov/citations/20230000714)** · NASA JSC, Lockheed Martin · 2023 · *paper*  
   Flight performance of Orion's Artemis I navigation system, built around four extended Kalman filters for atmospheric flight, Earth orbit, cislunar cruise and attitude, plus optical navigation and fault management. <sub>`flight` · Kalman filtering · state estimation</sub>
3. **[DART Guidance, Navigation and Control: System Performance and Challenges](https://airdrive.eventsair.com/eventsairwesteuprod/production-atpi-public/6f70f91b13ce4843a5e1056855f15df7)** · JHU APL, NASA · 2023 · *paper*  
   APL describes DART's three-axis attitude control and SMART Nav autonomous optical terminal guidance, including in-flight fixes for structural interaction and camera misalignment, ahead of the 2022 Dimorphos impact. <sub>`flight` · state estimation</sub>
4. **[The K2 Mission: Characterization and Early Results](https://arxiv.org/abs/1402.5163)** · NASA Ames, Ball Aerospace · 2014 · *paper*  
   After two reaction wheels failed, Kepler was flown pointing in its orbital plane so solar pressure balanced about roll, with thrusters trimming drift and unloading momentum, enabling K2. <sub>`operations` · fault-tolerant control</sub>
5. **[Spaceborne Autonomous Formation-Flying Experiment on the PRISMA Mission](https://doi.org/10.2514/1.55638)** · DLR, Swedish Space Corporation · 2012 · *paper*  
   DLR's SAFE experiment flew autonomous two-satellite formation control on PRISMA, pairing real-time differential-GPS relative navigation with impulsive relative-orbit maneuvers that kept formations accurate to better than 10 m. <sub>`flight` · Kalman filtering · optimal control</sub>
6. **[Zero-propellant maneuver guidance](https://doi.org/10.1109/MCS.2009.934089)** · Draper Laboratory, Naval Postgraduate School, NASA · 2009 · *paper*  
   Pseudospectral optimal attitude trajectories let the ISS control moment gyroscopes perform large rotations without thruster propellant, including a 180-degree turn of the station flown in March 2007. <sub>`operations` · optimal control · trajectory optimization</sub>
7. **[Hubble Space Telescope Reduced-Gyro Control Law Design, Implementation, and On-Orbit Performance](https://ntrs.nasa.gov/citations/20080023344)** · NASA GSFC, Lockheed Martin · 2008 · *paper*  
   After gyro failures, Hubble engineers built two- and one-gyro pointing modes that substitute magnetometers, star trackers and guidance sensors for missing rate axes, reaching 7 milliarcsecond stability or better. <sub>`operations` · fault-tolerant control · state estimation</sub>
8. **[Orbital Express Autonomous Rendezvous and Capture Flight Operations, Part 2 of 2: AR&C Exercise 4,5, and End-Of-Life](https://doi.org/10.2514/6.2008-6768)** · Boeing, DARPA · 2008 · *paper*  
   Boeing's operations account of the later DARPA Orbital Express exercises, in which the ASTRO servicer autonomously rendezvoused with and captured the NEXTSat client in orbit during 2007. <sub>`flight` · state estimation</sub>
9. **[Discovery of the Kalman filter as a practical tool for aerospace and industry](https://ntrs.nasa.gov/citations/19860003843)** · NASA Ames · 1985 · *report*  
   NASA Ames account of adapting Kalman's filter for Apollo circumlunar navigation, yielding the extended and square-root forms, and of its first airborne implementation and flight test. <sub>`flight` · Kalman filtering</sub>

**[back to top](#contents)**

### Aircraft flight control

1. **[Airbus concludes ATTOL with fully autonomous flight tests](https://www.airbus.com/en/newsroom/press-releases/2020-06-airbus-concludes-attol-with-fully-autonomous-flight-tests)** · Airbus · 2020 · *blog*  
   Airbus flew a commercial airliner through autonomous taxi, takeoff and landing guided by onboard image recognition, closing a two-year program of more than 500 test flights. <sub>`flight` · state estimation</sub>
2. **[F-35 Flight Control Law Design, Development and Verification](https://doi.org/10.2514/6.2018-3516)** · Lockheed Martin · 2018 · *paper*  
   Lockheed Martin recounts how F-35 flight control software, built on nonlinear dynamic inversion shared across three variants, was designed, verified and cleared through flight test into production. <sub>`production` · dynamic inversion</sub>
3. **[AIRBUS state of the art and practices on FDI and FTC in flight control system](https://doi.org/10.1016/j.conengprac.2010.12.009)** · Airbus · 2011 · *paper*  
   Airbus overview of how its in-service fly-by-wire flight controls detect, isolate and tolerate faults, covering monitoring design, redundancy management and the certification constraints shaping them. <sub>`production` · fault-tolerant control · state estimation</sub>
4. **[Flight Test of an L1 Adaptive Controller on the NASA AirSTAR Flight Test Vehicle](https://doi.org/10.2514/6.2010-8015)** · NASA Langley, UIUC · 2010 · *paper*  
   NASA Langley flew an L1 adaptive controller on the AirSTAR dynamically scaled transport model, evaluating its tracking and handling under nominal and deliberately degraded aircraft dynamics. <sub>`flight` · adaptive control</sub>
5. **[Flight Test Results from the NF-15B Intelligent Flight Control System (IFCS) Project with Adaptation to a Simulated Stabilator Failure](https://doi.org/10.2514/6.2007-2818)** · NASA Dryden · 2007 · *paper*  
   Piloted flight tests of NASA's NF-15B intelligent flight control system, a neural-network-adaptive dynamic inversion controller, compensating for a simulated stabilator failure. <sub>`flight` · adaptive control · dynamic inversion · fault-tolerant control</sub>
6. **[The X-43A Hyper-X Mach 7 Flight 2 Guidance, Navigation, and Control Overview and Flight Test Results](https://doi.org/10.2514/6.2005-3275)** · NASA Dryden, NASA Langley · 2005 · *paper*  
   Guidance, navigation and control design and flight results for NASA's X-43A, which separated from its booster and held its attitude through the March 2004 Mach 7 scramjet test. <sub>`flight` · gain scheduling</sub>
7. **[X-35B STOVL Flight Control Law Design and Flying Qualities](https://doi.org/10.2514/6.2002-6018)** · Lockheed Martin, BAE Systems · 2002 · *paper*  
   Lockheed Martin and BAE describe dynamic-inversion-based STOVL flight control for the X-35B, blending lift fan and nozzle effectors, with flying qualities from its hover and vertical-landing flights. <sub>`flight` · dynamic inversion</sub>
8. **[Triple-triple redundant 777 primary flight computer](https://doi.org/10.1109/AERO.1996.495891)** · Boeing · 1996 · *paper*  
   Boeing's 777 fly-by-wire primary flight computer uses three channels, each with three dissimilar processors, so flight control stays available after hardware or design faults in airline service. <sub>`production` · fault-tolerant control</sub>
9. **[AIRBUS A320/A330/A340 electrical flight controls - A family of fault-tolerant systems](https://doi.org/10.1109/FTCS.1993.627364)** · Airbus · 1993 · *paper*  
   Airbus's fly-by-wire architecture for the A320, A330 and A340, built from dissimilar redundant command and monitor computers so the production airliner family tolerates hardware and software faults. <sub>`production` · fault-tolerant control</sub>

**[back to top](#contents)**

### UAVs & drones

1. **[Autonomous navigation of stratospheric balloons using reinforcement learning](https://doi.org/10.1038/s41586-020-2939-8)** · Google, Loon · 2020 · *paper*  
   Google and Loon trained a deep reinforcement learning controller that steered superpressure balloons through stratospheric winds, beating Loon's prior controller in a 39-day Pacific flight experiment. <sub>`field` · reinforcement learning</sub>
2. **[Flight Control System for NASA's Mars Helicopter](https://dartslab.jpl.nasa.gov/References/pdf/2019-mars-heli.pdf)** · NASA JPL, NASA Ames · 2019 · *paper*  
   JPL details Ingenuity's 500 Hz rotor-pitch control loops, collective-to-motor feedforward and vision-inertial EKF navigation, validated in Mars-atmosphere chamber tests before the helicopter's flights on Mars. <sub>`flight` · Kalman filtering · feedforward · system identification</sub>
3. **[PX4: A Node-Based Multithreaded Open Source Robotics Framework for Deeply Embedded Platforms](https://doi.org/10.1109/ICRA.2015.7140074)** · ETH Zurich, PX4 · 2015 · *paper*  
   Introduces the PX4 publish-subscribe middleware and modular flight stack that run estimation and control on embedded autopilots, the open-source basis of many research and commercial drones. <sub>`production` · PID · state estimation</sub>

**[back to top](#contents)**

### Air traffic & collision avoidance

1. **[Next-Generation Airborne Collision Avoidance System](https://archive.ll.mit.edu/publications/journal/pdf/vol19_no1/19_1_1_Kochenderfer.pdf)** · MIT Lincoln Laboratory, FAA · 2012 · *paper*  
   ACAS X casts collision avoidance as a Markov decision process solved offline by dynamic programming into lookup tables; its ACAS Xa variant was approved for European airline carriage in 2025. <sub>`production` · dynamic programming · state estimation</sub>
2. **[Automatic Ground Collision Avoidance System design, integration, & flight test](https://doi.org/10.1109/MAES.2011.5871385)** · AFRL, NASA Dryden, Lockheed Martin · 2011 · *paper*  
   AFRL, NASA and Lockheed integrated and flight-tested F-16 automatic ground collision avoidance, which predicts recovery trajectories against terrain data and commands an autonomous fly-up when needed. <sub>`flight` · trajectory prediction</sub>
3. **[The Traffic Alert and Collision Avoidance System](https://archive.ll.mit.edu/publications/journal/pdf/vol16_no2/16_2_04Kuchar.pdf)** · MIT Lincoln Laboratory, FAA · 2007 · *paper*  
   Lincoln Laboratory overview of TCAS, the mandated airborne collision avoidance system on over 25,000 aircraft, covering transponder surveillance, threat detection and coordinated vertical resolution advisories. <sub>`operations` · rule-based logic</sub>

**[back to top](#contents)**

## Automotive, Rail & Maritime

Powertrain, chassis, driver assistance, autonomy, traffic flow, trains, and ships.

### Powertrain & energy management

1. **[Model Predictive Control of Turbocharged Gasoline Engines for Mass Production](https://doi.org/10.4271/2018-01-0875)** · GM, ODYS · 2018 · *paper*  
   Gain-scheduled linear MPC with Kalman filters coordinates throttle, wastegate and cam phasers to track torque in turbocharged gasoline engines, validated in GM production ECUs for 2018 production. <sub>`production` · MPC · gain scheduling · Kalman filtering · system identification</sub>
2. **[Supervisory Model Predictive Control of a Powertrain with a Continuously Variable Transmission](https://doi.org/10.4271/2018-01-0860)** · GM, ODYS · 2018 · *paper*  
   Supervisory gain-scheduled MPC jointly commands CVT ratio and engine torque to deliver driver-requested axle torque efficiently, identified from vehicle data and slated for GM production from 2018. <sub>`production` · MPC · gain scheduling · Kalman filtering</sub>
3. **[Automated Manual Transmissions](https://ieeecss.org/sites/ieeecss/files/2019-06/IoCT2-SS-Iannelli-1.pdf)** · University of Sannio, Fiat, BMW, Volkswagen · 2014 · *report*  
   Summarizes clutch-engagement control in production automated manual and dual-clutch transmissions (Fiat Selespeed, BMW SMG, VW DSG), which rely on gain-scheduled PID loops with feedforward. <sub>`production` · PID · feedforward · gain scheduling</sub>
4. **[Power Smoothing Energy Management and Its Application to a Series Hybrid Powertrain](https://doi.org/10.1109/TCST.2012.2218656)** · Ford, University of Michigan · 2013 · *paper*  
   Ford's series-hybrid energy management uses MPC to let the battery absorb engine power transients within charge limits, integrated into powertrain software and tested on a vehicle over UDDS. <sub>`field` · MPC</sub>
5. **[Battery Control Technology of Li-ion Battery System for HEV](https://global.honda/en/technical-review/PDF/024-1/024-1_72e.pdf)** · Honda · 2012 · *paper*  
   Honda's battery ECU for the lithium-ion Civic Hybrid estimates internal resistance, open-circuit voltage, SOC and capacity online, raising operating SOC only as the pack ages, and balances individual cells. <sub>`production` · state estimation · adaptive control</sub>
6. **[Model Predictive Idle Speed Control: Design, Analysis, and Experimental Evaluation](https://doi.org/10.1109/TCST.2011.2112361)** · Ford, University of Michigan, University of Trento · 2012 · *paper*  
   Ford engineers coordinated electronic throttle and spark timing with constrained MPC to hold engine idle speed, fitting production ECU limits and beating the baseline in vehicle tests. <sub>`field` · MPC</sub>
7. **[Model Based Air-path Management Control for Clean Diesel Engine](https://global.honda/en/technical-review/papers/10002345/)** · Honda, Keio University · 2009 · *paper*  
   Honda used MPC with a disturbance observer to jointly regulate diesel air mass flow and intake pressure through throttle and EGR valves, verified in on-vehicle tests. <sub>`field` · MPC · state estimation</sub>
8. **[Development of New-Generation Hybrid System THS II - Drastic Improvement of Power Performance and Fuel Economy](https://doi.org/10.4271/2004-01-0064)** · Toyota · 2004 · *paper*  
   Toyota engineers describe THS II, the power-split hybrid control system launched on the 2003 Prius, which coordinates engine and motor power to raise performance and fuel economy. <sub>`production` · optimal control</sub>
9. **[Super Ultra Low Emission System for the Accord SULEV](https://global.honda/en/technical-review/PDF/012-2/012-2_37e.pdf)** · Honda · 2000 · *paper*  
   Honda's Accord SULEV, the first SULEV-certified car on sale in the US, regulated air-fuel ratio with an online catalyst identifier, predictor and sliding mode controller on post-catalyst oxygen feedback. <sub>`production` · sliding mode · adaptive control · system identification</sub>

**[back to top](#contents)**

### Vehicle dynamics & chassis

1. **[Development of G-Vectoring Control Plus](https://www.mazda.com/globalassets/ja/assets/innovation/technology/gihou/2019/files/2019_no038.pdf)** · Mazda · 2019 · *paper*  
   Mazda extends its production G-Vectoring Control, which trims engine torque from steering-derived lateral jerk at turn-in, with brake-based yaw moment on corner exit, launched on the 2018 CX-5. <sub>`production` · feedforward</sub>
2. **[Automotive Engine-Based Traction Control](https://ieeecss.org/sites/ieeecss/files/2019-06/IoCT2-SS-Hrovat-1.pdf)** · Ford · 2014 · *report*  
   Ford's engine-only traction control regulates driven-wheel slip with a gain-scheduled PI-plus-lead loop derived from LQ design, shipping from 2006 on Fusion and F-150 models. <sub>`production` · LQR/LQG · PID · gain scheduling</sub>
3. **[Das vorausschauende aktive Fahrwerk der neuen S-Klasse](https://trid.trb.org/View/1359969)** · Daimler · 2013 · *paper*  
   Daimler engineers present Magic Body Control on the 2013 S-Class, where a stereo camera measures the road ahead so Active Body Control actuators pre-compensate body motion over bumps. <sub>`production` · feedforward · feedback control</sub>
4. **[Development of Electric Power Steering System for ATV](https://global.honda/en/technical-review/PDF/019-2/19-2_44e.pdf)** · Honda · 2007 · *paper*  
   Honda's EPS for the production 2007 FourTrax Foreman ATV combines torque-sensor assist, motor-speed damping, inertia compensation, thermal current limiting and assist gains scheduled on speed and drive mode. <sub>`production` · gain scheduling · feedforward</sub>
5. **[Predictive Active Steering Control for Autonomous Vehicle Systems](https://doi.org/10.1109/TCST.2007.894653)** · Ford, University of Sannio · 2007 · *paper*  
   Ford and Sannio researchers used nonlinear and successively linearized MPC to command active front steering for path following, tested on a vehicle on icy roads up to 21 m/s. <sub>`field` · nonlinear MPC · MPC</sub>
6. **[Active Body Control (ABC) The DaimlerChrysler Active Suspension and Damping System](https://saemobilus.sae.org/content/2002-21-0054)** · DaimlerChrysler · 2002 · *paper*  
   DaimlerChrysler engineers describe the production hydraulic active suspension tuned for S-Class and SL models, where 13 sensors feed control logic that shifts each wheel's spring base against roll and pitch. <sub>`production` · feedback control</sub>
7. **[Bosch ESP Systems: 5 Years of Experience](https://doi.org/10.4271/2000-01-1633)** · Bosch · 2000 · *paper*  
   Reviews five years of ESP field use, where estimated vehicle sideslip sets yaw-moment demands realized via individual wheel-slip control and engine intervention to prevent loss of control. <sub>`production` · state estimation</sub>
8. **[The development of vehicle stability control at Ford](https://doi.org/10.1109/3516.789681)** · Ford, Visteon · 1999 · *paper*  
   Ford and Visteon engineers describe practical problems in engineering Ford's yaw stability control, including driver-intent recognition, state and road-bank estimation, target generation, smooth brake actuation and fault detection. <sub>`production` · state estimation · fault-tolerant control</sub>
9. **[VDC, The Vehicle Dynamics Control System of Bosch](https://doi.org/10.4271/950759)** · Bosch · 1995 · *paper*  
   Bosch's vehicle dynamics control, later sold as ESP, compares driver-intended and measured yaw and lateral motion and corrects deviations via individual wheel brake pressures and engine torque. <sub>`production` · state estimation</sub>

**[back to top](#contents)**

### ADAS & autonomous driving

1. **[Are Commercially Implemented Adaptive Cruise Control Systems String Stable?](https://doi.org/10.1109/TITS.2020.3000682)** · Vanderbilt University, UIUC, University of Arizona, Rutgers University, Temple University · 2021 · *paper*  
   Over 1,200 miles of car-following tests on seven 2018 production ACC models, identified as delay-differential models, showed every system amplified speed disturbances along a platoon. <sub>`production` · system identification</sub>
2. **[End-to-end lateral planning](https://blog.comma.ai/end-to-end-lateral-planning/)** · comma.ai · 2021 · *blog*  
   comma.ai shipped a vision-trained policy that outputs 3D trajectories for openpilot's lateral control, trained in warped-video simulation and released to users in openpilot 0.8.3. <sub>`production` · learning-based control</sub>
3. **[Baidu Apollo Auto-Calibration System: An Industry-Level Data-Driven and Learning-Based Vehicle Longitude Dynamic Calibrating Algorithm](https://arxiv.org/abs/1808.10134)** · Baidu · 2018 · *paper*  
   Baidu builds longitudinal throttle and brake calibration tables from human driving data and refines them online, deployed on 100+ Apollo vehicles across over 2,000 hours of testing. <sub>`field` · learning-based control · system identification</sub>
4. **[Baidu Apollo EM Motion Planner](https://arxiv.org/abs/1807.08048)** · Baidu · 2018 · *paper*  
   Baidu's open-source Apollo planner alternates dynamic-programming and spline-QP optimization of path and speed in a Frenet frame, logging 3,380 hours of closed-loop driving on dozens of vehicles. <sub>`field` · dynamic programming · convex optimization · trajectory optimization</sub>
5. **[Heavy-Duty Vehicle Platooning for Sustainable Freight Transportation: A Cooperative Method to Enhance Safety and Efficiency](https://doi.org/10.1109/MCS.2015.2471046)** · Scania, KTH · 2015 · *paper*  
   Three Scania tractor-trailers ran decentralized cooperative adaptive cruise control on Sweden's E20 highway in public traffic, measuring follower fuel savings of roughly 4 to 6.5 percent. <sub>`field` · distributed control</sub>
6. **[Cooperative Adaptive Cruise Control in Real Traffic Situations](https://doi.org/10.1109/TITS.2013.2278494)** · UC Berkeley, Nissan · 2014 · *paper*  
   PATH and Nissan engineers fitted production cars with V2V-based cooperative adaptive cruise control and evaluated gap regulation and string stability in real highway traffic. <sub>`field` · feedforward · distributed control</sub>
7. **[Making Bertha Drive—An Autonomous Journey on a Historic Route](https://doi.org/10.1109/MITS.2014.2306552)** · Daimler, KIT, FZI · 2014 · *paper*  
   A Mercedes S-Class using near-production radar and stereo vision drove the 103 km Bertha Benz route autonomously, combining map-based localization with optimization-based urban motion planning. <sub>`field` · trajectory optimization · state estimation</sub>
8. **[Road Grade Estimation for Advanced Driver Assistance Systems](https://ieeecss.org/sites/ieeecss/files/2019-06/IoCT2-SS-Sahlholm-1.pdf)** · Scania, KTH · 2014 · *report*  
   Scania's production Active Prediction and Eco-roll use mapped road grade to plan truck speed and coasting over hills; the authors propose Kalman-filtered fleet estimates to build those maps. <sub>`production` · Kalman filtering · state estimation</sub>
9. **[Look-ahead control for heavy trucks to minimize trip time and fuel consumption](https://doi.org/10.1016/j.conengprac.2008.07.005)** · Linköping University, Scania · 2009 · *paper*  
   Dynamic programming over GPS and a road-slope map produced velocity setpoints for a heavy truck's cruise controller, cutting fuel use in highway trials with a real truck. <sub>`field` · dynamic programming · MPC</sub>

**[back to top](#contents)**

### Traffic & mobility

1. **[Traffic Control via Connected and Automated Vehicles (CAVs): An Open-Road Field Experiment with 100 CAVs](https://doi.org/10.1109/MCS.2024.3498552)** · CIRCLES Consortium, UC Berkeley, Vanderbilt University · 2025 · *paper*  
   A centralized speed planner sent LTE targets to 100 mixed-make vehicles whose onboard controllers overrode stock ACC, testing stop-and-go wave smoothing in rush-hour I-24 traffic near Nashville. <sub>`field` · optimal control · reinforcement learning · distributed control</sub>
2. **[Dissipation of stop-and-go waves via control of autonomous vehicles: Field experiments](https://arxiv.org/abs/1705.01693)** · UIUC, Rutgers University, Temple University, University of Arizona, Inria · 2018 · *paper*  
   In ring-road experiments with over 20 cars, controlling one autonomous vehicle's speed damped spontaneously forming stop-and-go waves, reducing braking events and fuel consumption. <sub>`field` · PID</sub>
3. **[Smart Urban Signal Networks: Initial Application of the SURTRAC Adaptive Traffic Signal Control System](https://ojs.aaai.org/index.php/ICAPS/article/view/13594)** · Carnegie Mellon University · 2013 · *paper*  
   CMU's decentralized SURTRAC schedules each intersection's phases in real time and shares planned outflows with neighbors, cutting travel time about 26% across nine Pittsburgh intersections. <sub>`field` · dynamic programming · distributed control</sub>
4. **[Heuristic Ramp-Metering Coordination Strategy Implemented at Monash Freeway, Australia](https://doi.org/10.3141/2178-02)** · Technical University of Crete, VicRoads · 2010 · *paper*  
   VicRoads deployed HERO, which coordinates per-ramp ALINEA regulators with queue control and Kalman estimates, on Melbourne's Monash Freeway, raising peak speeds and throughput before wider rollout. <sub>`operations` · PID · Kalman filtering · distributed control</sub>
5. **[ALINEA Local Ramp Metering: Summary of Field Results](https://doi.org/10.3141/1603-12)** · Technical University of Crete, INRETS, Rijkswaterstaat · 1997 · *paper*  
   Summarizes field results of ALINEA, an integral-type local ramp-metering feedback regulator on occupancy, at single and multiple ramps on Paris's Boulevard Périphérique and Amsterdam's A10. <sub>`operations` · PID</sub>
6. **[SCOOT - A Traffic Responsive Method of Coordinating Signals](https://www.trl.co.uk/uploads/trl/documents/LR1014.pdf)** · TRRL · 1981 · *report*  
   TRRL's SCOOT continuously models detector-measured traffic and incrementally adjusts signal splits, offsets and cycles, cutting delay about 12% versus fixed-time plans in Glasgow and Coventry trials. <sub>`field` · optimal control · state estimation</sub>
7. **[The Sydney coordinated adaptive traffic (SCAT) system philosophy and benefits](https://doi.org/10.1109/T-VT.1980.23833)** · NSW Department of Main Roads · 1980 · *paper*  
   New South Wales road engineers set out the design and benefits of SCAT, which adapts signal cycle, split and offset to detector data across Sydney's network. <sub>`operations` · adaptive control</sub>

**[back to top](#contents)**

### Rail

1. **[Trip Optimizer for Railroads](https://ieeecss.org/sites/ieeecss/files/2019-06/IoCT2-SS-Eldredge-1.pdf)** · GE Transportation, GE Global Research · 2014 · *report*  
   GE's onboard Trip Optimizer plans fuel-minimal locomotive throttle profiles under arrival-time and speed constraints with adaptive parameter estimation, logging over 150 million revenue miles and 4-17% savings. <sub>`operations` · optimal control · Kalman filtering · adaptive control</sub>
2. **[Energy-efficient train control](https://doi.org/10.1016/0967-0661(94)90198-8)** · University of South Australia · 1994 · *paper*  
   Applies optimal control to find energy-minimizing suburban train driving strategies that keep to the timetable, the research behind the Metromiser driver-advice system used on suburban trains. <sub>`operations` · optimal control</sub>
3. **[Automatic train operation system based on predictive fuzzy control](https://doi.org/10.1109/AIIA.1988.13336)** · Hitachi · 1988 · *paper*  
   Hitachi's ATO encodes skilled drivers' rules in a predictive fuzzy controller for train speed and stopping, matching expert operators in trials on Sendai's municipal subway. <sub>`operations` · fuzzy logic</sub>

**[back to top](#contents)**

### Maritime

1. **[Autonomous maritime collision avoidance: Field verification of autonomous surface vehicle behavior in challenging scenarios](https://doi.org/10.1002/rob.21919)** · NTNU, Maritime Robotics · 2020 · *paper*  
   An MPC collision-avoidance system weighing collision risk against COLREGs compliance steered an autonomous surface vessel through North Sea encounter scenarios in a Deltares-organized verification trial. <sub>`field` · MPC</sub>
2. **[Passive nonlinear observer design for ships using Lyapunov methods: full-scale experiments with a supply vessel](https://doi.org/10.1016/S0005-1098(98)00121-6)** · NTNU · 1999 · *paper*  
   A passivity-based nonlinear observer filters wave-frequency motion and estimates ship velocities and bias forces for dynamic positioning, demonstrated in full-scale trials with an offshore supply vessel. <sub>`field` · state estimation</sub>
3. **[Rudder Roll Stabilization for Ships](https://ris.utwente.nl/ws/files/171144967/Amerongen90rudder.pdf)** · University of Twente, Van Rietschoten & Houwens, TU Delft, Royal Netherlands Navy · 1990 · *paper*  
   LQG rudder control with automatic gain control damped ship roll in full-scale sea trials, after which the Royal Netherlands Navy chose to fit rudder roll stabilization to ships under construction. <sub>`field` · LQR/LQG · adaptive control</sub>
4. **[A Dynamic Positioning System Based on Kalman Filtering and Optimal Control](https://doi.org/10.4173/mic.1980.3.1)** · NTNU, SINTEF, Kongsberg · 1980 · *paper*  
   NTNU, SINTEF and Kongsberg present a vessel dynamic positioning system using Kalman-filter estimates of motion and environmental forces with optimal feedback and wind feedforward, supported by operational recordings. <sub>`operations` · Kalman filtering · LQR/LQG · feedforward</sub>

**[back to top](#contents)**

## Robotics

Legged machines, humanoids, manipulators, mobile and aerial robots, and robots that work on or near people.

### Legged locomotion

1. **[Starting on the Right Foot with Reinforcement Learning](https://bostondynamics.com/blog/starting-on-the-right-foot-with-reinforcement-learning/)** · Boston Dynamics · 2024 · *blog*  
   Boston Dynamics embedded an RL-trained locomotion policy within Spot's existing MPC controller, replacing parallel MPC instances, and shipped it to customers in software release 4.0. <sub>`production` · reinforcement learning · MPC</sub>
2. **[Perceptive Locomotion Through Nonlinear Model-Predictive Control](https://doi.org/10.1109/TRO.2023.3275384)** · ETH Zurich · 2023 · *paper*  
   Nonlinear MPC for ANYmal that converts perceived terrain into convex foothold regions and signed-distance collision constraints, validated by dynamic climbing over rough terrain on the real robot. <sub>`field` · nonlinear MPC</sub>
3. **[Learning robust perceptive locomotion for quadrupedal robots in the wild](https://doi.org/10.1126/scirobotics.abk2822)** · ETH Zurich, KAIST, Intel · 2022 · *paper*  
   ANYmal policy fusing proprioception with exteroceptive height maps through a learned belief encoder, deployed outdoors across seasons and finishing an hour-long Alpine hike in human-recommended time. <sub>`field` · reinforcement learning · state estimation</sub>
4. **[Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning](https://roboticsproceedings.org/rss17/p061.html)** · Oregon State University · 2021 · *paper*  
   Cassie biped learned blind stair traversal through sim-to-real RL with randomized stair terrain, relying only on proprioception to handle diverse real-world staircases. <sub>`field` · reinforcement learning</sub>
5. **[RMA: Rapid Motor Adaptation for Legged Robots](https://arxiv.org/abs/2107.04034)** · UC Berkeley, Carnegie Mellon University, Meta · 2021 · *paper*  
   Unitree A1 quadruped combines an RL base policy with an online adaptation module estimating environment factors from proprioceptive history, walking zero-shot on sand, grass, stairs, and slippery ground. <sub>`field` · reinforcement learning · adaptive control</sub>
6. **[Learning quadrupedal locomotion over challenging terrain](https://doi.org/10.1126/scirobotics.abc5986)** · ETH Zurich, KAIST, Intel · 2020 · *paper*  
   Proprioceptive ANYmal controller trained by teacher-student RL with a terrain curriculum, deployed zero-shot over mud, snow, rubble, vegetation, and flowing water in natural field trials. <sub>`field` · reinforcement learning · imitation learning</sub>
7. **[Learning agile and dynamic motor skills for legged robots](https://doi.org/10.1126/scirobotics.aau5872)** · ETH Zurich, Intel · 2019 · *paper*  
   ANYmal locomotion policies trained with RL in simulation, using a learned actuator network for realism, transferred to hardware for faster running and fall recovery beyond prior model-based controllers. <sub>`field` · reinforcement learning · system identification</sub>
8. **[Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](https://doi.org/10.1109/IROS.2018.8594448)** · MIT · 2018 · *paper*  
   Cheetah 3 quadruped runs multiple gaits, galloping up to 3 m/s on hardware, using a single-rigid-body MPC that solves a convex QP for ground reaction forces at 25-50 Hz. <sub>`field` · MPC · convex optimization</sub>

**[back to top](#contents)**

### Humanoids & whole-body control

1. **[Large Behavior Models and Atlas Find New Footing](https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/)** · Boston Dynamics, Toyota Research Institute · 2025 · *blog*  
   A roughly 450M-parameter language-conditioned diffusion transformer, trained mainly on VR teleoperation data, controls the full Atlas humanoid at 30 Hz for long-horizon manipulation such as sorting Spot parts on hardware. <sub>`field` · imitation learning · whole-body control</sub>
2. **[Training a Whole-Body Control Foundation Model](https://www.agilityrobotics.com/content/training-a-whole-body-control-foundation-model)** · Agility Robotics · 2025 · *blog*  
   Agility trained a sub-million-parameter LSTM whole-body controller for Digit purely with RL in Isaac Sim, transferring zero-shot to hardware for walking and heavy object handling. <sub>`field` · reinforcement learning · whole-body control</sub>
3. **[Learning agile soccer skills for a bipedal robot with deep reinforcement learning](https://doi.org/10.1126/scirobotics.adi8022)** · Google DeepMind · 2024 · *paper*  
   Miniature humanoids learned agile soccer skills through deep RL and skill distillation in simulation, then transferred zero-shot to real robots playing one-versus-one matches. <sub>`field` · reinforcement learning</sub>
4. **[Real-world humanoid locomotion with reinforcement learning](https://doi.org/10.1126/scirobotics.adi9579)** · UC Berkeley · 2024 · *paper*  
   Causal transformer policy trained by large-scale RL in randomized simulation, deployed zero-shot on the full-size Digit humanoid outdoors on sidewalks, grass, and slopes while rejecting pushes. <sub>`field` · reinforcement learning</sub>
5. **[Picking Up Momentum](https://bostondynamics.com/blog/picking-up-momentum/)** · Boston Dynamics · 2023 · *blog*  
   Atlas MPC extended from centroidal dynamics to individual joints, link momenta, and carried-object forces, letting the hydraulic humanoid toss a tool bag mid-jump and carry planks. <sub>`field` · MPC · whole-body control</sub>
6. **[Flipping the Script with Atlas](https://bostondynamics.com/blog/flipping-the-script-with-atlas/)** · Boston Dynamics · 2021 · *blog*  
   Atlas parkour pairs a library of offline trajectory-optimized behavior templates with one online MPC that adapts and chains them to perceived obstacles during real course runs. <sub>`field` · trajectory optimization · MPC</sub>
7. **[Optimization-based locomotion planning, estimation, and control design for the atlas humanoid robot](https://doi.org/10.1007/s10514-015-9479-3)** · MIT · 2016 · *paper*  
   MIT's DARPA Robotics Challenge software for Atlas couples a QP walking controller using time-varying LQR cost-to-go with a LIDAR-aided EKF, enabling precise rough-terrain walking in post-Trials lab experiments. <sub>`field` · convex optimization · LQR/LQG · Kalman filtering · whole-body control</sub>
8. **[Team IHMC's Lessons Learned from the DARPA Robotics Challenge Trials](https://doi.org/10.1002/rob.21571)** · IHMC · 2015 · *paper*  
   IHMC's momentum-based walking controller and coactive operator interface guided Boston Dynamics' Atlas to second place at the 2013 DARPA Robotics Challenge Trials. <sub>`field` · whole-body control</sub>
9. **[The development of Honda humanoid robot](https://doi.org/10.1109/ROBOT.1998.677288)** · Honda · 1998 · *paper*  
   Honda's early humanoid prototypes walked on stairs and uneven floors by stabilizing offline gait patterns with floor reaction force, ZMP, and foot-placement control, the basis for ASIMO. <sub>`field` · ZMP control · feedforward</sub>

**[back to top](#contents)**

### Manipulation & industrial arms

1. **[Deep RL at Scale: Sorting Waste in Office Buildings with a Fleet of Mobile Manipulators](https://arxiv.org/abs/2305.03270)** · Google, Everyday Robots · 2023 · *paper*  
   Deep RL waste-sorting policy trained and evaluated on 23 mobile manipulators across three office buildings over two years, blending simulation and real-world experience. <sub>`field` · reinforcement learning</sub>
2. **[The Franka Emika Robot: A Reference Platform for Robotics Research and Education](https://doi.org/10.1109/MRA.2021.3138382)** · Franka Emika · 2022 · *paper*  
   Describes the commercial Franka Emika Panda arm, with torque sensing in all seven joints and a 1 kHz torque control interface enabling impedance control, widely sold to labs. <sub>`production` · impedance control</sub>
3. **[Learning dexterous in-hand manipulation](https://doi.org/10.1177/0278364919887447)** · OpenAI · 2020 · *paper*  
   Shadow Dexterous Hand learned vision-based in-hand object reorientation with RL and heavy domain randomization entirely in simulation, then executed the skill on the physical hand. <sub>`field` · reinforcement learning</sub>
4. **[QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation](https://arxiv.org/abs/1806.10293)** · Google, X, UC Berkeley · 2018 · *paper*  
   Closed-loop vision-based grasping learned by scalable off-policy Q-learning from 580k real grasp attempts on seven KUKA arms, reaching 96% success on unseen objects. <sub>`field` · reinforcement learning</sub>
5. **[The DLR lightweight robot: design and control concepts for robots in human environments](https://doi.org/10.1108/01439910710774386)** · DLR · 2007 · *paper*  
   Outlines joint-torque sensing, impedance control, and collision handling on the DLR lightweight arm, whose technology was transferred to KUKA's commercial lightweight robot line. <sub>`production` · impedance control</sub>

**[back to top](#contents)**

### Mobile, warehouse & field robots

1. **[Development of a sweet pepper harvesting robot](https://doi.org/10.1002/rob.21937)** · Wageningen University & Research, Ben-Gurion University, Umeå University · 2020 · *paper*  
   SWEEPER sweet pepper harvester guides a six-axis arm and custom end effector with eye-in-hand vision, field-tested in a commercial greenhouse with reported harvest success rates and cycle times. <sub>`field` · visual servoing</sub>
2. **[Coordinating Hundreds of Cooperative, Autonomous Vehicles in Warehouses](https://doi.org/10.1609/aimag.v29i1.2082)** · Kiva Systems · 2008 · *paper*  
   Kiva drive units ferry inventory pods under a centralized job manager with grid A* path planning and heuristic allocation, operating commercially in warehouses with over 100 robots. <sub>`production` · distributed control</sub>
3. **[Robots at the tipping point: the road to iRobot Roomba](https://doi.org/10.1109/MRA.2006.1598056)** · iRobot · 2006 · *paper*  
   An iRobot engineer recounts how Roomba became a mass-market floor-cleaning robot by relying on low-cost sensing and reactive behavior-based coverage control rather than mapping. <sub>`production` · behavior-based control</sub>

**[back to top](#contents)**

### Aerial robotics

1. **[Champion-level drone racing using deep reinforcement learning](https://doi.org/10.1038/s41586-023-06419-4)** · University of Zurich, Intel · 2023 · *paper*  
   Quadrotor racing policy trained with deep RL in simulation plus data-driven residual models, flying on onboard sensing and winning head-to-head races against three human champions, including two world champions. <sub>`field` · reinforcement learning · state estimation</sub>
2. **[Neural-Fly enables rapid learning for agile flight in strong winds](https://doi.org/10.1126/scirobotics.abm6597)** · Caltech · 2022 · *paper*  
   Quadrotor controller pairs an offline meta-learned aerodynamic basis with online composite adaptation, cutting tracking error in wind-tunnel winds up to 12 m/s and in outdoor flights. <sub>`field` · adaptive control · learning-based control</sub>
3. **[Inside the mind of the Skydio 2](https://medium.com/skydio/inside-the-mind-of-the-skydio-2-b1b78aa6dfa7)** · Skydio · 2019 · *blog*  
   Explains how the Skydio 2 consumer drone fuses six fisheye cameras into motion estimates and 3D maps, then runs a 500 Hz multi-objective planner for autonomous tracking and avoidance. <sub>`production` · trajectory optimization · state estimation</sub>
4. **[A platform for aerial robotics research and demonstration: The Flying Machine Arena](https://doi.org/10.1016/j.mechatronics.2013.11.006)** · ETH Zurich · 2014 · *paper*  
   ETH's motion-capture quadrocopter testbed with latency-compensating estimation, cascaded feedback-linearizing control, and iterative learning, supporting over 100 public demonstration events in 2011-2012. <sub>`field` · dynamic inversion · iterative learning control · state estimation</sub>

**[back to top](#contents)**

### Surgical robots

1. **[RIO: Robotic-Arm Interactive Orthopedic System MAKOplasty: User Interactive Haptic Orthopedic Robotics](https://doi.org/10.1007/978-1-4419-1126-1_10)** · MAKO Surgical · 2011 · *paper*  
   Describes MAKO's haptic robotic arm for knee arthroplasty, which confines the surgeon-guided cutting tool within CT-planned virtual boundaries, used in clinical procedures. <sub>`clinical` · impedance control · virtual fixtures</sub>
2. **[The Intuitive™ telesurgery system: overview and application](https://doi.org/10.1109/ROBOT.2000.844121)** · Intuitive Surgical · 2000 · *paper*  
   Intuitive Surgical engineers describe the da Vinci master-slave telesurgery system, its teleoperation architecture for minimally invasive instruments, and its early clinical application. <sub>`clinical` · teleoperation</sub>

**[back to top](#contents)**

### Entertainment robots

1. **[Olaf: Bringing an Animated Character to Life in the Physical World](https://arxiv.org/abs/2512.16705)** · Disney Research · 2025 · *paper*  
   Olaf character walks with animation-guided RL policies that include actuator temperature feedback and footstep-noise rewards, validated on hardware ahead of 2026 Disney park debuts. <sub>`field` · reinforcement learning · imitation learning</sub>
2. **[Design and Control of a Bipedal Robotic Character](https://roboticsproceedings.org/rss20/p103.html)** · Disney Research, Walt Disney Imagineering · 2024 · *paper*  
   Bipedal character controlled by RL policies imitating artist-authored animation, with an animation engine and operator interface enabling live puppeteering in real-time show performances. <sub>`field` · reinforcement learning · imitation learning</sub>

**[back to top](#contents)**

### Space & underwater robots

1. **[Ocean One: A Robotic Avatar for Oceanic Discovery](https://doi.org/10.1109/MRA.2016.2613281)** · Stanford, KAUST, DRASSM · 2016 · *paper*  
   Bimanual humanoid diving robot combining whole-body control with haptic teleoperation, used to recover artifacts from the 17th-century La Lune shipwreck at roughly 90 m depth. <sub>`field` · whole-body control · teleoperation</sub>
2. **[Robonaut 2 - The first humanoid robot in space](https://doi.org/10.1109/ICRA.2011.5979830)** · NASA, GM · 2011 · *paper*  
   Describes NASA and GM's dexterous humanoid with torque-sensing compliant joints and impedance control, built for and delivered to the International Space Station in 2011. <sub>`flight` · impedance control</sub>

**[back to top](#contents)**

## Process Industries & Manufacturing

Refineries, chemical and paper plants, metals, pharmaceuticals, semiconductors, and precision mechatronics.

### Refining & chemicals

1. **[Origins of Dynamic Matrix Control: The Early Writings of Charles R. Cutler](https://psecommunity.org/LAPSE:2025.0700)** · NTNU, Shell · 2025 · *report*  
   Annotated collection of Charles Cutler's early writings tracing Dynamic Matrix Control from his thesis ideas to its 1973 trials on the catalytic cracker at Shell's New Orleans refinery. <sub>`production` · MPC</sub>
2. **[APC advances FCC unit performance at Pemex Deer Park refinery](https://digitalrefining.com/article/1003151/apc-advances-fcc-unit-performance-at-pemex-deer-park-refinery)** · Pemex Deer Park, KBC · 2024 · *paper*  
   Pemex Deer Park replaced separate SMOC MPC, RTO and quality-estimator tools on its FCC unit with one integrated PACE application spanning over 25 manipulated and 71 controlled variables. <sub>`operations` · MPC · real-time optimization</sub>
3. **[Rigorous Non-Linear Optimization in Dow's Hydrocarbons Business](https://aiche.org/conferences/aiche-spring-meeting-and-global-congress-on-process-safety/2017/proceeding/paper/2d-rigorous-non-linear-optimization-dows-hydrocarbons-business)** · Dow · 2017 · *talk*  
   Dow reviews the rigorous nonlinear real-time optimization running across most of its steam cracker fleet, covering its support model, performance metrics and the case for first-principles plant models. <sub>`operations` · real-time optimization</sub>
4. **[Ethylene Plantwide Control and Optimization](https://ieeecss.org/sites/ieeecss/files/2019-06/IoCT2-SS-Lu-1.pdf)** · Honeywell · 2014 · *report*  
   Honeywell's Profit Optimizer coordinates 15 to 30 Profit Controller MPCs per ethylene plant using successively linearized dynamic models, with typical production gains worth 1.5 to 3 million dollars yearly. <sub>`operations` · MPC · real-time optimization</sub>
5. **[NLMPC: A Platform for Optimal Control of Feed- or Product-Flexible Manufacturing](https://doi.org/10.1007/978-3-540-72699-9_30)** · ExxonMobil · 2007 · *paper*  
   ExxonMobil Chemical's in-house nonlinear MPC, built on fundamental state-space models solved by SQP, has handled regulatory and grade-transition control on industrial polymerization plants since 1994. <sub>`operations` · nonlinear MPC</sub>
6. **[Quadratic Programming Solution of Dynamic Matrix Control (QDMC)](https://doi.org/10.1080/00986448608911397)** · Shell · 1986 · *paper*  
   Shell extended DMC to handle input and output constraints by solving a quadratic program online, reporting a pyrolysis furnace temperature application and other Shell unit deployments. <sub>`production` · MPC · convex optimization</sub>
7. **[Model Predictive Heuristic Control: Applications to Industrial Processes](https://doi.org/10.1016/0005-1098(78)90001-8)** · ADERSA · 1978 · *paper*  
   ADERSA's IDCOM predictive heuristic control was applied on an FCC distillation column, a 250 MW steam generator, and a PVC plant, an early industrial MPC report. <sub>`production` · MPC</sub>

**[back to top](#contents)**

### Pulp & paper

1. **[Feedback controller design for a spatially distributed system: the paper machine problem](https://doi.org/10.1109/TCST.2003.816420)** · Honeywell, University of British Columbia · 2003 · *paper*  
   Honeywell's 2D loop-shaping design for cross-directional paper machine control became a commercial tuning tool and retuned controllers on two industrial machines, stabilizing one of them. <sub>`production` · robust control · distributed control</sub>
2. **[Practical aspects of model predictive control implementation on an industrial lime kiln](https://doi.org/10.23919/ECC.1997.7082518)** · Noranda, James Maclaren · 1997 · *paper*  
   Constrained MPC was implemented on a pulp mill rotary lime kiln to regulate the temperature profile and excess oxygen, targeting lime quality, energy use, and TRS emissions. <sub>`production` · MPC</sub>
3. **[Successful adaptive control of paper machines](https://doi.org/10.1016/0005-1098(75)90008-4)** · ASEA · 1975 · *paper*  
   ASEA engineers report adaptive self-tuning regulators running on industrial paper machine quality loops, an early account of adaptive control succeeding in mill operation. <sub>`production` · adaptive control</sub>
4. **[Computer Control of a Paper Machine—an Application of Linear Stochastic Control Theory](https://doi.org/10.1147/rd.114.0389)** · IBM, Billerud · 1967 · *paper*  
   Minimum variance controllers built from maximum likelihood identified process and disturbance models regulated a Billerud paper machine, reporting results from on-line computer control. <sub>`production` · LQR/LQG · system identification</sub>

**[back to top](#contents)**

### Metals, mining & cement

1. **[Performance Assessments of an Advanced Control System in an Iron Ore Industrial Grinding Circuit](https://doi.org/10.3390/min15111172)** · Usiminas, ANDRITZ, University of São Paulo · 2025 · *paper*  
   ANDRITZ BrainWave MPC with fuzzy supervisory logic on an Usiminas iron ore ball-mill circuit, assessed in a 67-day on/off test, raised throughput about 5% and cut energy use. <sub>`production` · MPC · fuzzy logic</sub>
2. **[Multi-Mode Model Predictive Control Approach for Steel Billets Reheating Furnaces](https://doi.org/10.3390/s23083966)** · Marche Polytechnic University, Alperia Green Future · 2023 · *paper*  
   A multi-mode MPC with a billet-tracking virtual sensor runs steel reheating furnaces through production, shutdowns, and restarts, installed at several European steel plants with energy savings. <sub>`production` · MPC · state estimation</sub>
3. **[Model predictive control of a rotary cement kiln](https://doi.org/10.1016/j.conengprac.2010.08.004)** · ABB, Holcim · 2011 · *paper*  
   ABB's Expert Optimizer MPC was commissioned on a Holcim cement kiln in Switzerland, running above 95% uptime and sharply reducing feed rate and burning-zone temperature variance. <sub>`production` · MPC</sub>
4. **[Thinking ahead: Ensuring stable and more beneficial operation of a cement plant with Expert Optimizer](https://library.e.abb.com/public/76155f7ed7ce01ea8325734b0040c552/18-21%203M772_ENG72dpi.pdf)** · ABB, Holcim · 2007 · *report*  
   ABB applied receding-horizon MPC in Expert Optimizer to hold precalciner temperature with primary fuels at Holcim's Lägerdorf cement plant, outperforming manual operator control. <sub>`production` · MPC</sub>
5. **[Industrial applications of predictive functional control to metallurgical industries](https://doi.org/10.1109/CCA.1995.555880)** · ADERSA · 1995 · *paper*  
   ADERSA reports industrial applications of predictive functional control in metallurgical plants, covering how PFC is implemented and the results obtained by users. <sub>`production` · MPC</sub>
6. **[Report on Actual Benefits Arising From The Application of Expert Control Systems in Industrial Semi-Autogenous Grinding Circuits](https://doi.org/10.1016/S1474-6670(17)53088-8)** · Control International · 1989 · *paper*  
   Control International documents realized benefits from rule-based expert control systems running on industrial semi-autogenous grinding mill circuits. <sub>`production` · expert systems</sub>

**[back to top](#contents)**

### Pharmaceuticals

1. **[Implementation of a fully integrated continuous manufacturing line for direct compression and coating at a commercial pharmaceutical facility – Part 1: Operational considerations and control strategy](https://doi.org/10.1016/j.ijpharm.2023.122820)** · Merck, MSD · 2023 · *paper*  
   Merck/MSD built a continuous direct-compression and coating line in a commercial plant, controlled through real-time monitoring, residence-time models, automated NIR testing, and automatic material diversion. <sub>`production` · state estimation</sub>
2. **[The Application of an Automated Control Strategy for an Integrated Continuous Pharmaceutical Pilot Plant](https://doi.org/10.1021/op500104d)** · MIT · 2015 · *paper*  
   MIT ran an automated control strategy on an end-to-end continuous pharmaceutical pilot plant, holding critical material attributes of the API slurry near setpoints during sustained operation. <sub>`field` · PID</sub>

**[back to top](#contents)**

### Semiconductors & precision motion

1. **[Control of Wafer Scanners: Methods and Developments](https://doi.org/10.23919/ACC45564.2020.9147464)** · ASML, Cymer · 2020 · *paper*  
   ASML and Cymer engineers review control in production wafer scanners, from light-source and reticle-stage control to vibration isolation, thermal modeling, and deformation control. <sub>`production` · system identification · state estimation · robust control</sub>
2. **[Enhancing Flatbed Printer Accuracy and Throughput: Optimal Rational Feedforward Controller Tuning Via Iterative Learning Control](https://doi.org/10.1109/TIE.2016.2613498)** · Eindhoven University of Technology, Océ · 2017 · *paper*  
   TU/e and Océ tune rational feedforward controllers through iterative learning control, improving accuracy and throughput in experiments on an industrial flatbed inkjet printer. <sub>`field` · iterative learning control · feedforward</sub>
3. **[HVM capabilities of CPE run-to-run overlay control](https://doi.org/10.1117/12.2190852)** · GlobalFoundries, KLA · 2015 · *paper*  
   GlobalFoundries and KLA run per-exposure run-to-run overlay correction in high-volume 28nm and 14nm manufacturing, cutting mean plus 3-sigma overlay by up to 20% on critical layers. <sub>`production` · run-to-run control</sub>
4. **[Position Control in Lithographic Equipment](https://doi.org/10.1109/MCS.2011.941882)** · ASML · 2011 · *paper*  
   ASML engineer explains how wafer and reticle stages in lithography scanners reach nanometer positioning, decoupling six-degree-of-freedom actuation so SISO feedback and feedforward controllers suffice. <sub>`production` · PID · feedforward</sub>
5. **[A brief history of disk drive control](https://doi.org/10.1109/MCS.2002.1003997)** · Agilent, Stanford · 2002 · *paper*  
   History of hard disk drive servo control co-written by an industry engineer, tracing how seek and track-following loops in shipped drives evolved alongside heads, actuators, and media. <sub>`production` · state estimation · PID</sub>
6. **[Automatic control in microelectronics manufacturing: Practices, challenges, and possibilities](https://doi.org/10.1016/S0005-1098(00)00084-4)** · UT Austin, Texas Instruments, AMD, Motorola, Hyundai · 2000 · *paper*  
   Engineers from Texas Instruments, AMD, Motorola and Hyundai with UT Austin survey fab control practice, including run-to-run control of lithography, etch, deposition, and CMP in production. <sub>`production` · run-to-run control</sub>
7. **[Run by run control of chemical-mechanical polishing](https://doi.org/10.1109/3476.558560)** · MIT, University of Michigan, SEMATECH · 1996 · *paper*  
   An EWMA run-by-run controller with a multivariate recipe generator compensated removal-rate drift in chemical-mechanical polishing, validated on more than one CMP tool over several months. <sub>`field` · run-to-run control</sub>

**[back to top](#contents)**

### Oil & gas production

1. **[Control Requirements for Automatic Managed Pressure Drilling System](https://doi.org/10.2118/119442-PA)** · Statoil · 2010 · *paper*  
   Statoil sets out requirements for automatic downhole pressure control by topside choking in managed pressure drilling, drawing on its 2007 automatic MPD operation on Kvitebjørn. <sub>`field` · PID · state estimation</sub>
2. **[Improving Oil Production Using Smart Fields Technology in the SF30 Satellite Oil Development Offshore Malaysia](https://doi.org/10.4043/16162-MS)** · Shell, WellDynamics · 2004 · *paper*  
   Shell's SF30 offshore Malaysia field combined smart well completions with intelligent gas-lift optimization and real-time flow estimation, producing since 2001 with estimated 10% production gains. <sub>`operations` · real-time optimization · state estimation</sub>

**[back to top](#contents)**

## Energy, Buildings & Infrastructure

Power grids, renewables, fusion, data centers, buildings, storage, and water networks.

### Power grids & storage

1. **[Hornsdale Power Reserve Expansion Virtual Machine Mode Actual vs Modelled Study](https://arena.gov.au/assets/2023/09/HPRX-VMM-Modelled-vs-Actual-Report.pdf)** · Neoen, Tesla · 2023 · *report*  
   Tesla's Virtual Machine Mode let the 150 MW Hornsdale battery provide synthetic inertia, and its measured response to an August 2022 frequency dip closely matched modelled behaviour. <sub>`operations` · grid-forming control</sub>
2. **[AI-Driven Smart Community Control for Accelerating PV Adoption and Enhancing Grid Resilience](https://www.nrel.gov/docs/fy22osti/82576.pdf)** · NREL, Holy Cross Energy · 2022 · *talk*  
   Home energy management and aggregator controls dispatched batteries, heat pump water heaters and thermostats in net-zero homes in Basalt, Colorado, shifting load out of the utility's peak window. <sub>`field` · MPC</sub>
3. **[Balancing and Frequency Control](https://www.nerc.com/comm/RSTC_Reliability_Guidelines/Reference_Document_NERC_Balancing_and_Frequency_Control.pdf)** · NERC · 2021 · *report*  
   NERC explains how North American balancing authorities control frequency, from governor droop response to AGC acting on area control error with frequency bias, judged by CPS1 and BAAL. <sub>`operations` · droop control · feedback control</sub>
4. **[Dalrymple ESCRI-SA Battery Energy Storage Project](https://www.electranet.com.au/wp-content/uploads/2021/01/ESCRI-SA-presentation-to-SEPA-Energy-Storage-WG-April-2020.pdf)** · ElectraNet, ABB · 2020 · *talk*  
   ElectraNet and ABB describe a 30 MW grid-forming virtual-generator battery that kept a South Australian regional network supplied through planned and unplanned islanding events. <sub>`operations` · grid-forming control · droop control</sub>
5. **[Real-Time Optimization and Control of Next-Generation Distribution Infrastructure](https://www.nrel.gov/docs/fy21osti/78742.pdf)** · NREL, Southern California Edison, Holy Cross Energy · 2020 · *talk*  
   NREL slides on real-time optimal power flow controllers for DERs, field-demonstrated for voltage regulation and virtual power plant operation at Stone Edge Farm microgrid and Holy Cross Energy homes. <sub>`field` · distributed control · convex optimization</sub>
6. **[Design of the Pacific DC Intertie Wide Area Damping Controller](https://doi.org/10.1109/TPWRS.2019.2903782)** · Sandia National Laboratories, Bonneville Power Administration, Montana Tech · 2019 · *paper*  
   Engineers designed a PMU-feedback controller that modulates Pacific DC Intertie power flow to damp inter-area oscillations, validated through open- and closed-loop tests on the Western Interconnection. <sub>`field` · wide-area control</sub>
7. **[PDCI Damping Controller Test Results and Project Summary](https://www.sandia.gov/research/publications/details/pdci-damping-controller-test-results-and-project-summary-2019-05-01/)** · Sandia National Laboratories, Bonneville Power Administration, Montana Tech · 2019 · *report*  
   Final project report analyzing grid tests where real-time PMU feedback modulated HVDC power on the Pacific DC Intertie, assessing added oscillation damping and safe operation. <sub>`field` · wide-area control</sub>
8. **[Experimental Demonstration of Frequency Regulation by Commercial Buildings—Part II: Results and Performance Evaluation](https://doi.org/10.1109/TSG.2016.2628893)** · UC Berkeley, LBNL, ETH Zurich · 2018 · *paper*  
   A test-cell air handler at LBNL's FLEXLAB tracked a PJM regulation signal using hierarchical robust MPC and fan-speed control, with tracking accuracy and occupant comfort measured experimentally. <sub>`field` · MPC · robust control · Kalman filtering</sub>
9. **[Initial operation of the Hornsdale Power Reserve Battery Energy Storage System](https://www.aemo.com.au/-/media/Files/Media_Centre/2018/Initial-operation-of-the-Hornsdale-Power-Reserve.pdf)** · AEMO · 2018 · *report*  
   AEMO review of the grid battery's first months, showing faster, more precise AGC regulation tracking than a steam unit and contingency frequency response during a real generator trip. <sub>`operations` · droop control</sub>
10. **[Implementation and Rationale for PJM's Conditional Neutrality Regulation Signals](https://www.pjm.com/-/media/committees-groups/task-forces/rmistf/postings/regulation-market-whitepaper.ashx)** · PJM · 2017 · *report*  
   PJM's January 2017 AGC redesign runs a PI controller on area control error, splitting output via low-pass filters into slow RegA and fast RegD signals with conditional storage payback. <sub>`operations` · PID · feedback control</sub>
11. **[Pacific Northwest GridWise™ Testbed Demonstration Projects; Part I. Olympic Peninsula Project](https://www.pnnl.gov/publications/pacific-northwest-gridwisetm-testbed-demonstration-projects-part-i-olympic-peninsula)** · PNNL · 2008 · *report*  
   Field demonstration where thermostats, water heaters, building HVAC, municipal pumps and generators bid against five-minute price signals to relieve feeder congestion and reduce peak demand. <sub>`field` · distributed control · transactive control</sub>

**[back to top](#contents)**

### Wind & solar

1. **[Collective wind farm operation based on a predictive model increases utility-scale energy production](https://doi.org/10.1038/s41560-022-01085-8)** · MIT, Caltech, ReNew Power · 2022 · *paper*  
   Researchers working with ReNew Power deployed predictive-model-based collective yaw control at a utility-scale wind farm, measuring higher energy production than standard greedy turbine operation. <sub>`field` · setpoint optimization</sub>
2. **[Field experiment for open-loop yaw-based wake steering at a commercial onshore wind farm in Italy](https://doi.org/10.5194/wes-6-159-2021)** · TU Delft, GE Renewable Energy, Enel Green Power, TU Munich · 2021 · *paper*  
   At Enel's Sardinian wind farm, GE turbines applied FLORIS lookup-table yaw offsets, toggled against baseline every 35 minutes, yielding gains up to 35% in some directions and losses elsewhere. <sub>`field` · setpoint optimization</sub>
3. **[Results from a wake-steering experiment at a commercial wind plant: investigating the wind speed dependence of wake-steering performance](https://doi.org/10.5194/wes-6-1427-2021)** · NREL, ENGIE · 2021 · *paper*  
   NREL and ENGIE offset the wind-vane signal fed to an unmodified Senvion turbine's yaw controller at a French wind plant, cutting wake losses about 6% over three months. <sub>`field` · setpoint optimization</sub>
4. **[Initial results from a field campaign of wake steering applied at a commercial wind farm – Part 1](https://doi.org/10.5194/wes-4-273-2019)** · NREL, NextEra Energy Resources · 2019 · *paper*  
   At a NextEra commercial wind farm, two turbines followed FLORIS-designed yaw offset schedules, raising downstream turbine energy about 14% in a narrow sector and pair output about 4%. <sub>`field` · setpoint optimization</sub>
5. **[Wind farm power optimization through wake steering](https://doi.org/10.1073/pnas.1903680116)** · Stanford · 2019 · *paper*  
   A wake model calibrated on historical operating data was used to optimize yaw misalignment by gradient ascent, then field-tested at an Alberta wind farm with statistically significant power gains. <sub>`field` · setpoint optimization · system identification</sub>
6. **[Demonstration of Essential Reliability Services by a 300-MW Solar Photovoltaic Power Plant](https://www.osti.gov/biblio/1349211)** · NREL, CAISO, First Solar · 2017 · *report*  
   CAISO, First Solar and NREL tested a 300 MW PV plant's controls on the live grid, demonstrating AGC following, droop frequency response, ramp limiting and voltage regulation. <sub>`field` · droop control</sub>
7. **[Field test of wake steering at an offshore wind farm](https://doi.org/10.5194/wes-2-229-2017)** · NREL, Envision Energy · 2017 · *paper*  
   NREL and Envision modified yaw controllers on turbines at a commercial offshore wind farm in China to apply FLORIS-optimized wake steering, measuring power gains comparable to model predictions. <sub>`field` · setpoint optimization</sub>
8. **[Advanced Grid-Friendly Controls Demonstration Project for Utility-Scale PV Power Plants](https://www.osti.gov/biblio/1236761)** · NREL, AES, First Solar · 2016 · *report*  
   NREL and plant owners field-tested active power controls on utility-scale PV plants in Puerto Rico and Texas, covering frequency regulation, variability smoothing and power quality support. <sub>`field` · droop control</sub>
9. **[Field testing of linear individual pitch control on the two-bladed controls advanced research turbine](https://www.osti.gov/biblio/1239055)** · TU Delft, NREL · 2016 · *paper*  
   TU Delft and NREL field-tested linear individual pitch control, gain-scheduled on rotor speed, on the two-bladed CART2 turbine, significantly reducing periodic loads below and above rated wind. <sub>`field` · gain scheduling</sub>
10. **[Field Testing of Feedforward Collective Pitch Control on the CART2 Using a Nacelle-Based Lidar Scanner](https://nrel.gov/docs/fy15osti/55222.pdf)** · NREL, University of Stuttgart · 2014 · *paper*  
   On NREL's CART2 turbine, a feedforward pitch term driven by nacelle lidar wind preview cut generator speed variation about 30% and tower loads about 10% when correlation was good. <sub>`field` · feedforward</sub>

**[back to top](#contents)**

### Data centers

1. **[Simulator-based reinforcement learning for data center cooling optimization](https://engineering.fb.com/2024/09/10/data-center-engineering/simulator-based-reinforcement-learning-for-data-center-cooling-optimization/)** · Meta · 2024 · *blog*  
   Meta trained an RL agent in a thermal simulator and piloted it controlling supply-airflow setpoints in a live data center, cutting fan energy about 20% while staying within temperature limits. <sub>`field` · reinforcement learning</sub>
2. **[Carbon-Aware Computing for Datacenters](https://arxiv.org/abs/2106.11750)** · Google · 2021 · *paper*  
   Google's fleet-wide system forecasts grid carbon intensity and demand, then solves a risk-aware day-ahead optimization to cap flexible compute hourly, shifting load toward cleaner hours in production. <sub>`production` · stochastic optimization</sub>
3. **[Data center cooling using model-predictive control](https://research.google/pubs/data-center-cooling-using-model-predictive-control/)** · Google · 2018 · *paper*  
   Google identified a data-driven dynamics model of a server floor within hours of exploration and used it in MPC to regulate temperatures and airflow, outperforming the existing controllers. <sub>`field` · MPC · system identification · reinforcement learning</sub>
4. **[Safety-first AI for autonomous data centre cooling and industrial control](https://deepmind.google/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/)** · Google DeepMind, Google · 2018 · *blog*  
   Cloud-based neural-network system directly sets cooling actions every five minutes in multiple Google data centres, with local safety verification and operator override, reaching about 30% energy savings. <sub>`production` · learning-based control</sub>
5. **[DeepMind AI Reduces Google Data Centre Cooling Bill by 40%](https://deepmind.google/discover/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/)** · Google DeepMind, Google · 2016 · *blog*  
   Neural-network ensembles predicting PUE, temperature and pressure produced cooling recommendations that, in live tests at a Google data centre, cut cooling energy by roughly 40 percent. <sub>`field` · learning-based control</sub>

**[back to top](#contents)**

### Buildings & HVAC

1. **[Commercial building HVAC demand flexibility with model predictive control: Field demonstration and literature insights](https://doi.org/10.1016/j.enbuild.2025.116097)** · LBNL · 2025 · *paper*  
   LBNL ran price-responsive MPC on a large Berkeley office building's HVAC across four seasons, using thermal mass to cut HVAC demand 40-65% during high-price periods versus rule-based control. <sub>`field` · MPC</sub>
2. **[Controlling Commercial Cooling Systems Using Reinforcement Learning](https://arxiv.org/abs/2211.07357)** · Google DeepMind, Google, Trane Technologies · 2022 · *paper*  
   DeepMind, Google and Trane extended data-center RL control to commercial building cooling plants, running live experiments at two facilities that saved roughly 9% and 13% energy. <sub>`field` · reinforcement learning</sub>
3. **[eco+ Thermostat Optimization Pilot](https://www.ecobee.com/ecoplusemv)** · ecobee, Demand Side Analytics · 2020 · *report*  
   Randomized evaluation across roughly 240,000 ecobee thermostats of personalized pre-cooling, setback and scheduling algorithms, measuring about 1 kW demand-response reduction per device and 5-6% energy savings. <sub>`production` · learning-based control</sub>
4. **[Model Predictive Climate Control of a Swiss Office Building: Implementation, Results, and Cost-Benefit Analysis](https://doi.org/10.1109/TCST.2015.2415411)** · ETH Zurich · 2016 · *paper*  
   ETH Zurich implemented MPC for the climate control system of an occupied Swiss office building, reporting measured comfort and energy performance plus a cost-benefit analysis of deployment. <sub>`field` · MPC</sub>
5. **[Experimental analysis of model predictive control for an energy efficient building heating system](https://doi.org/10.1016/j.apenergy.2011.03.009)** · University of West Bohemia, Czech Technical University in Prague, ETH Zurich · 2011 · *paper*  
   Weather-forecast-based MPC ran the heating system of a real Prague building during a two-month experiment, with energy use compared against the conventional heating controller. <sub>`field` · MPC</sub>

**[back to top](#contents)**

### Nuclear & fusion

1. **[Avoiding fusion plasma tearing instability with deep reinforcement learning](https://doi.org/10.1038/s41586-024-07024-9)** · Princeton University, PPPL · 2024 · *paper*  
   An RL controller deployed on the DIII-D tokamak adjusted actuators in real time to keep predicted tearing-instability likelihood below a threshold while sustaining H-mode performance. <sub>`field` · reinforcement learning</sub>
2. **[Towards practical reinforcement learning for tokamak magnetic control](https://arxiv.org/abs/2307.11546)** · Google DeepMind, EPFL · 2023 · *paper*  
   Follow-up work improving RL magnetic controllers' shape accuracy, plasma-current bias and training time, with the gains validated in new discharges on the TCV tokamak. <sub>`field` · reinforcement learning</sub>
3. **[Magnetic control of tokamak plasmas through deep reinforcement learning](https://doi.org/10.1038/s41586-021-04301-9)** · Google DeepMind, EPFL · 2022 · *paper*  
   A deep RL policy trained in simulation directly commanded the TCV tokamak's magnetic coils, producing and holding a variety of plasma shapes in real experimental discharges. <sub>`field` · reinforcement learning</sub>

**[back to top](#contents)**

### Water & wastewater

1. **[Full-scale implementation of an advanced control system on a biological wastewater treatment plant](https://doi.org/10.1016/j.ifacol.2016.07.360)** · Aalto University, Mipro · 2016 · *paper*  
   A dynamic matrix controller regulating effluent ammonia through aeration, plus PCA-based sensor monitoring, ran six months at a full-scale activated-sludge plant and lowered aeration energy. <sub>`operations` · MPC</sub>
2. **[Control of Large-Scale Irrigation Networks](https://doi.org/10.1109/JPROC.2006.887289)** · University of Melbourne · 2007 · *paper*  
   Melbourne researchers present system identification and decentralized feedback design for automating gravity-fed irrigation channels in Victoria, the approach behind Rubicon's commercially deployed Total Channel Control. <sub>`production` · distributed control · system identification</sub>
3. **[Systems Engineering for Irrigation Systems: Successes and Challenges](https://skoge.folk.ntnu.no/prost/proceedings/ifac2005/Fullpapers/05174.pdf)** · University of Melbourne · 2005 · *paper*  
   Overview of irrigation canal automation covering closed-loop system identification and decentralized PI-plus-feedforward water-level control, illustrated with field data from Victoria's Haughton Main Canal. <sub>`field` · PID · feedforward · distributed control · system identification</sub>

**[back to top](#contents)**

## Computing, Networks & Marketplaces

Feedback inside software. Congestion control, video streaming, autoscaling, overload protection, ad pacing, and operations.

### Congestion control & networking

1. **[PLB: Congestion Signals are Simple and Effective for Network Load Balancing](https://research.google/pubs/plb-congestion-signals-are-simple-and-effective-for-network-load-balancing/)** · Google · 2022 · *paper*  
   Hosts repath congested connections by rehashing the IPv6 flow label when congestion signals persist; used fleetwide at Google, cutting switch utilization imbalance 60% and drops 33%. <sub>`production` · event-triggered control · distributed control</sub>
2. **[Swift: Delay is Simple and Effective for Congestion Control in the Datacenter](https://research.google/pubs/swift-delay-is-simple-and-effective-for-congestion-control-in-the-datacenter/)** · Google · 2020 · *paper*  
   Delay-target AIMD window control for datacenter transport, deployed in Google datacenters, holding short-RPC tail latency near 50 microseconds at 100 Gbps per server under near-full load. <sub>`production` · AIMD</sub>
3. **[Evaluating COPA congestion control for improved video performance](https://engineering.fb.com/2019/11/17/video-engineering/copa/)** · Meta · 2019 · *blog*  
   A/B tests of the delay-targeting Copa controller over QUIC on live Facebook Live uploads, cutting P90 app RTT 27% versus CUBIC and beating BBR on goodput. <sub>`field` · queueing control</sub>
4. **[A Google Congestion Control Algorithm for Real-Time Communication](https://datatracker.ietf.org/doc/html/draft-ietf-rmcat-gcc-02)** · Google, Politecnico di Bari · 2016 · *standard*  
   Specifies WebRTC's delay-based rate control: a Kalman filter tracks queuing-delay trend, an adaptive-threshold overuse detector, and AIMD rate updates, shipped in Chrome since M23 and Hangouts. <sub>`production` · Kalman filtering · AIMD</sub>
5. **[BBR: Congestion-Based Congestion Control](https://queue.acm.org/detail.cfm?id=3022184)** · Google · 2016 · *paper*  
   Paces TCP senders from running estimates of bottleneck bandwidth and minimum RTT; all Google B4 WAN TCP traffic moved to BBR, and YouTube trials cut median RTT 53%. <sub>`production` · state estimation · queueing control</sub>
6. **[Congestion Control for Large-Scale RDMA Deployments](https://www.microsoft.com/en-us/research/publication/congestion-control-for-large-scale-rdma-deployments/)** · Microsoft, Mellanox · 2015 · *paper*  
   DCQCN, an ECN-driven RoCEv2 rate controller implemented in Mellanox NICs and tuned with a fluid model of the closed loop, was being deployed across Microsoft datacenters at publication. <sub>`production` · AIMD</sub>

**[back to top](#contents)**

### Video streaming & adaptive bitrate

1. **[Learning in situ: a randomized experiment in video streaming](https://www.usenix.org/conference/nsdi20/presentation/yan)** · Stanford · 2020 · *paper*  
   Fugu couples an MPC bitrate controller with a transmission-time predictor trained on live data, evaluated in a randomized trial on the public Puffer service with 63,508 viewers. <sub>`field` · MPC · learning-based control</sub>
2. **[Real-world Video Adaptation with Reinforcement Learning](https://arxiv.org/abs/2008.12858)** · Meta, MIT · 2020 · *paper*  
   Trains RL bitrate-adaptation policies for Facebook's web video player and tests them in a week-long worldwide deployment covering over 30 million streaming sessions. <sub>`production` · reinforcement learning</sub>
3. **[A Buffer-Based Approach to Rate Adaptation: Evidence from a Large Video Streaming Service](https://doi.org/10.1145/2619239.2626296)** · Netflix, Stanford · 2014 · *paper*  
   Picks video bitrate as a function of playback buffer occupancy instead of throughput forecasts. A/B tests in the Netflix client with millions of users cut rebuffers 10-20%. <sub>`production` · queueing control</sub>

**[back to top](#contents)**

### Autoscaling & resource management

1. **[What's new with Robinhood, our in-house load balancing service](https://dropbox.tech/infrastructure/robinhood-in-house-load-balancing-service)** · Dropbox · 2024 · *blog*  
   A PID controller per node adjusts endpoint weights toward the service's mean utilization; running in every Dropbox datacenter, it shrank some large fleets by 25%. <sub>`production` · PID · distributed control</sub>
2. **[Transparent memory offloading: more memory at a fraction of the cost and power](https://engineering.fb.com/2022/06/20/data-infrastructure/transparent-memory-offloading-more-memory-at-a-fraction-of-the-cost-and-power/)** · Meta · 2022 · *blog*  
   Senpai proportionally sets memory reclaim from how far kernel pressure-stall readings sit below target, offloading cold pages; across millions of Meta servers it saved 20-32% memory. <sub>`production` · PID</sub>
3. **[Autopilot: workload autoscaling at Google](https://doi.org/10.1145/3342195.3387524)** · Google · 2020 · *paper*  
   Automatically sets task counts and per-task CPU and memory limits from usage history; jobs on it cover 48% of fleet usage, halving slack and cutting severe OOMs tenfold. <sub>`production` · learning-based control · adaptive control</sub>
4. **[Thunderbolt: Throughput-Optimized, Quality-of-Service-Aware Power Capping at Scale](https://www.usenix.org/conference/osdi20/presentation/li-shaohong)** · Google · 2020 · *paper*  
   Two-threshold multiplicative-decrease, randomized-unthrottle CPU bandwidth control throttles batch tasks to keep power safe; running in multiple Google clusters, enabling 9-25% oversubscription. <sub>`production` · AIMD</sub>
5. **[Unimog - Cloudflare's edge load balancer](https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/)** · Cloudflare · 2020 · *blog*  
   A control loop reassigns forwarding-table buckets so each edge server's measured load converges to a common level; in production over a year with visibly uniform CPU. <sub>`production` · feedback control</sub>
6. **[Software-defined far memory in warehouse-scale computers](https://research.google/pubs/software-defined-far-memory-in-warehouse-scale-computers/)** · Google · 2019 · *paper*  
   Compresses cold pages under a promotion-rate SLO, with node agents and fleet-level autotuning adjusting coldness thresholds; deployed across Google since 2016, serving thousands of services. <sub>`production` · learning-based control</sub>
7. **[PerfIso: Performance Isolation for Commercial Latency-Sensitive Services](https://www.usenix.org/conference/atc18/presentation/iorgulescu)** · Microsoft · 2018 · *paper*  
   Grows or shrinks batch-job cores to hold a buffer of idle cores for Bing search; used three years on 90,000+ servers, lifting off-peak CPU use from 21% to 66%. <sub>`production` · feedback control</sub>
8. **[Dynamo: Facebook's Data Center-Wide Power Management System](https://research.facebook.com/publications/dynamo-facebooks-data-center-wide-power-management-system/)** · Meta · 2016 · *paper*  
   Hierarchical power-capping controllers with three-band hysteresis sample power every few seconds; run in all Facebook datacenters, preventing 18 potential outages in six months. <sub>`production` · distributed control · event-triggered control</sub>
9. **[Kraken: Leveraging Live Traffic Tests to Identify and Resolve Resource Utilization Bottlenecks in Large Scale Web Services](https://www.usenix.org/conference/osdi16/technical-sessions/presentation/veeraraghavan)** · Meta · 2016 · *paper*  
   Shifts live user traffic onto target clusters in steps, monitoring latency and error feedback to stop before unhealthy load; in production three years, raising utilization over 20%. <sub>`production` · feedback control</sub>
10. **[Making Facebook's software infrastructure more energy efficient with Autoscale](https://engineering.fb.com/2014/08/08/production-engineering/making-facebook-s-software-infrastructure-more-energy-efficient-with-autoscale/)** · Meta · 2014 · *blog*  
   A PI controller, tuned on a fitted piecewise-linear CPU-versus-load model, sizes the active web-server pool; production clusters saved 10-15% power daily, up to 27% overnight. <sub>`production` · PID · system identification</sub>

**[back to top](#contents)**

### Load shedding & overload control

1. **[Cinnamon Auto-Tuner: Adaptive Concurrency in the Wild](https://www.uber.com/blog/cinnamon-auto-tuner-adaptive-concurrency-in-the-wild/)** · Uber · 2023 · *blog*  
   A TCP-Vegas-style loop with filtered p90 latency and Little's-law checks tunes inflight limits; during a real downstream slowdown it throttled traffic and averted cascading failure. <sub>`production` · queueing control · adaptive control</sub>
2. **[Cinnamon: Using Century Old Tech to Build a Mean Load Shedder](https://www.uber.com/blog/cinnamon-using-century-old-tech-to-build-a-mean-load-shedder/)** · Uber · 2023 · *blog*  
   Uber's Go load shedder uses a PID loop to set the request rejection fraction by priority; production tests held goodput near capacity at 300% overload. <sub>`production` · PID · queueing control</sub>
3. **[Hodor: Overload scenarios and the evolution of their detection and handling](https://engineering.linkedin.com/blog/2023/hodor--overload-scenarios-and-the-evolution-of-their-detection-a)** · LinkedIn · 2023 · *blog*  
   Adds GC and threadpool-wait detectors plus latency confirmation, escalating priority-tiered shedding until recovery; runs on 1000+ LinkedIn services and has stopped hundreds of overloads. <sub>`production` · queueing control</sub>
4. **[Amazon DynamoDB: A Scalable, Predictably Performant, and Fully Managed NoSQL Database Service](https://www.usenix.org/conference/atc22/presentation/elhemali)** · AWS · 2022 · *paper*  
   Reports DynamoDB's token-bucket admission control, proportional-control adaptive capacity that boosted throttled partitions, and later global admission control, used in the managed production service. <sub>`production` · PID · distributed control</sub>
5. **[Hodor: Detecting and addressing overload in LinkedIn microservices](https://engineering.linkedin.com/blog/2022/hodor--detecting-and-addressing-overload-in-linkedin-microservic)** · LinkedIn · 2022 · *blog*  
   Detects CPU overload from heartbeat-thread delays and adapts a concurrency limit with probing and exponential backoff; onboarded across most LinkedIn microservices, starting with flagship Voyager. <sub>`production` · adaptive control</sub>
6. **[Introducing QALM, Uber's QoS Load Management Framework](https://www.uber.com/blog/qalm-qos-load-management-framework/)** · Uber · 2018 · *blog*  
   CoDel-style per-endpoint queues detect overload from minimum queueing delay and shed requests by criticality; adopted by core Uber production services as YARPC middleware. <sub>`production` · queueing control</sub>
7. **[Overload Control for Scaling WeChat Microservices](https://arxiv.org/abs/1806.04075)** · Tencent · 2018 · *paper*  
   DAGOR flags overload from average queuing time and moves a priority admission threshold with multiplicative decrease and additive increase; ran five years in WeChat's backend. <sub>`production` · AIMD · queueing control</sub>
8. **[Performance Under Load](https://netflixtechblog.medium.com/performance-under-load-3e6fa9a60581)** · Netflix · 2018 · *blog*  
   Adapts server concurrency limits from a latency gradient borrowed from TCP congestion control, rejecting excess requests, as part of a Netflix production rollout. <sub>`production` · queueing control · adaptive control</sub>
9. **[Handling Overload](https://sre.google/sre-book/handling-overload/)** · Google · 2016 · *report*  
   Google SRE chapter on client-side adaptive throttling: clients compare requests to backend accepts and reject locally with rising probability, keeping overloaded backends stable in production. <sub>`production` · distributed control</sub>
10. **[Fail at Scale: Reliability in the face of rapid change](https://queue.acm.org/detail.cfm?id=2839461)** · Meta · 2015 · *paper*  
   Describes Facebook's CoDel-variant queue timeouts plus adaptive LIFO for overloaded servers, built into Wangle/Thrift and HHVM and used broadly with fixed defaults. <sub>`production` · queueing control</sub>

**[back to top](#contents)**

### Ads, marketplaces & inventory

1. **[Smart Fast Finish: Preventing Overdelivery via Daily Budget Pacing at DoorDash](https://arxiv.org/abs/2509.07929)** · DoorDash · 2025 · *paper*  
   Sets each campaign's end-of-day throttle ramp from its historical overspend, guarding against a positive feedback loop; in use at DoorDash, an A/B test cut overdelivery from 7.0% to 4.7%. <sub>`production` · adaptive control · feedforward</sub>
2. **[A Better Match for Drivers and Riders: Reinforcement Learning at Lyft](https://arxiv.org/abs/2310.13810)** · Lyft · 2023 · *paper*  
   Online RL learns driver future-earnings values in real time to steer rider-driver matching; switchback tests in most markets preceded a 2021 global rollout worth $30M+ yearly. <sub>`production` · reinforcement learning · dynamic programming</sub>
3. **[Deep Inventory Management](https://arxiv.org/abs/2210.03137)** · Amazon · 2022 · *paper*  
   Model-based deep RL through a differentiable simulator sets periodic-review buy quantities; a 26-week randomized trial on about 10K products cut inventory 12% with unchanged revenue. <sub>`production` · reinforcement learning · optimal control</sub>
4. **[Deep Reinforcement Learning for Sponsored Search Real-time Bidding](https://arxiv.org/abs/1803.00259)** · Alibaba · 2018 · *paper*  
   Formulates hourly bid-model selection as a robust MDP solved by deep RL, extended to multiple agents; deployed on Alibaba's e-commerce search auctions with online A/B testing. <sub>`production` · reinforcement learning</sub>
5. **[Feedback Control of Real-Time Display Advertising](https://arxiv.org/abs/1603.01055)** · UCL, YOYI, BigTree · 2016 · *paper*  
   Compares PID and water-level controllers that adjust RTB bids to hold KPIs such as eCPC at reference; PID ran live on the BigTree mobile DSP with A/B gains. <sub>`production` · PID</sub>
6. **[Smart Pacing for Effective Online Ad Campaign Optimization](https://arxiv.org/abs/1506.05851)** · Yahoo · 2015 · *paper*  
   Adjusts layered, response-rate-tiered bid probabilities each slot from spend feedback to pace budgets; deployed in Yahoo's DSP, online A/B tests cut eCPC up to 79%. <sub>`production` · feedback control · adaptive control</sub>
7. **[Budget Pacing for Targeted Online Advertisements at LinkedIn](https://doi.org/10.1145/2623330.2623366)** · LinkedIn · 2014 · *paper*  
   Throttles each campaign's auction participation rate, tuned against a spend plan built from forecast supply, so budgets last the day; evaluated in experiments on LinkedIn's ad marketplace. <sub>`production` · feedback control · feedforward</sub>

**[back to top](#contents)**

## Healthcare & Agriculture

Automated insulin delivery, anesthesia and ventilation, neuromodulation, prosthetics, and closed-loop agriculture.

### Glucose control & insulin delivery

1. **[Multicenter, Randomized Trial of a Bionic Pancreas in Type 1 Diabetes](https://doi.org/10.1056/NEJMoa2205225)** · Beta Bionics, Massachusetts General Hospital, Boston University, Jaeb Center for Health Research · 2022 · *paper*  
   Pivotal 13-week trial of the iLet bionic pancreas, initialized only from body weight and self-adapting its insulin dosing, which lowered HbA1c and led to FDA clearance. <sub>`clinical` · MPC · adaptive control</sub>
2. **[Open-Source Automated Insulin Delivery in Type 1 Diabetes](https://doi.org/10.1056/nejmoa2203913)** · University of Otago, OpenAPS · 2022 · *paper*  
   CREATE randomized trial of community-built AndroidAPS running the OpenAPS predictive dosing algorithm, showing better time in range than sensor-augmented pumps over 24 weeks. <sub>`clinical` · rule-based logic</sub>
3. **[Randomized Trial of Closed-Loop Control in Very Young Children with Type 1 Diabetes](https://doi.org/10.1056/nejmoa2111673)** · University of Cambridge, CamDiab · 2022 · *paper*  
   Multinational crossover trial of the CamAPS FX adaptive MPC app in children aged 1 to 7, improving glucose time in range at home without more hypoglycemia. <sub>`clinical` · MPC · adaptive control</sub>
4. **[A Real-World Prospective Study of the Safety and Effectiveness of the Loop Open Source Automated Insulin Delivery System](https://doi.org/10.1089/dia.2020.0535)** · Jaeb Center for Health Research, Tidepool, Stanford · 2021 · *paper*  
   Six-month observational study of 558 users of the DIY Loop iPhone app, which forecasts glucose and adjusts pump insulin, reporting gains in time in range. <sub>`clinical` · MPC</sub>
5. **[Improved Glycemic Outcomes With Medtronic MiniMed Advanced Hybrid Closed-Loop Delivery: Results From a Randomized Crossover Trial Comparing Automated Insulin Delivery With Predictive Low Glucose Suspend in People With Type 1 Diabetes](https://doi.org/10.2337/dc20-2250)** · Medtronic, University of Otago · 2021 · *paper*  
   Randomized crossover home trial of the MiniMed 780G advanced hybrid loop, adding automatic correction boluses to PID-based basal control, versus predictive low-glucose suspend alone. <sub>`clinical` · PID</sub>
6. **[Multicenter Trial of a Tubeless, On-Body Automated Insulin Delivery System With Customizable Glycemic Targets in Pediatric and Adult Participants With Type 1 Diabetes](https://doi.org/10.2337/dc21-0172)** · Insulet, University of Virginia · 2021 · *paper*  
   Pivotal three-month study of Omnipod 5, a patch pump running an on-board predictive controller with user-selectable targets, in 241 children and adults, supporting its FDA clearance. <sub>`clinical` · MPC</sub>
7. **[Evaluation of Automatic Class III Designation for Control-IQ Technology](https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN190034.pdf)** · FDA, Tandem Diabetes Care · 2019 · *report*  
   FDA De Novo decision memo for Control-IQ, which forecasts glucose 30 minutes ahead and resets basal insulin every five minutes, creating the interoperable automated glycemic controller device class. <sub>`production` · MPC</sub>
8. **[Six-Month Randomized, Multicenter Trial of Closed-Loop Control in Type 1 Diabetes](https://doi.org/10.1056/NEJMoa1907863)** · University of Virginia, Tandem Diabetes Care, Jaeb Center for Health Research · 2019 · *paper*  
   Pivotal iDCL trial of Control-IQ, a UVA-derived predictive controller modulating pump insulin from CGM, which raised time in range over sensor-augmented pumps across six months at home. <sub>`clinical` · MPC</sub>
9. **[Closed-Loop Insulin Delivery for Glycemic Control in Noncritical Care](https://doi.org/10.1056/nejmoa1805233)** · University of Cambridge, University of Bern · 2018 · *paper*  
   Randomized ward trial applying the Cambridge MPC insulin controller to hospitalized type 2 diabetes patients on general wards, improving glucose control over usual subcutaneous insulin therapy. <sub>`clinical` · MPC</sub>
10. **[Closed-loop insulin delivery in suboptimally controlled type 1 diabetes: a multicentre, 12-week randomised trial](https://doi.org/10.1016/s0140-6736(18)31947-0)** · University of Cambridge · 2018 · *paper*  
   Randomized UK/US free-living trial of the Cambridge model predictive controller in day-and-night hybrid closed loop, raising time in range about 11 points over sensor-augmented pumps. <sub>`clinical` · MPC</sub>
11. **[Safety of a Hybrid Closed-Loop Insulin Delivery System in Patients With Type 1 Diabetes](https://doi.org/10.1001/jama.2016.11708)** · Medtronic, International Diabetes Center · 2016 · *paper*  
   Pivotal outpatient study of the MiniMed 670G, whose PID controller with insulin feedback automates basal delivery; its safety results underpinned the first FDA approval of a hybrid closed loop. <sub>`clinical` · PID</sub>
12. **[Space GlucoseControl system for blood glucose control in intensive care patients - a European multicentre observational study](https://doi.org/10.1186/s12871-016-0175-4)** · B. Braun, Charles University · 2016 · *paper*  
   Seventeen-centre ICU study of B. Braun's commercial pump-integrated enhanced MPC insulin advisor in 508 patients, keeping glucose in target 83% of the time with rare severe hypoglycaemia. <sub>`clinical` · MPC</sub>
13. **[The Effect of Insulin Feedback on Closed Loop Glucose Control](https://doi.org/10.1210/jc.2010-2578)** · Medtronic, Boston Children's Hospital · 2011 · *paper*  
   Inpatient study of Medtronic's PID insulin controller augmented with model-estimated plasma insulin feedback, the design lineage later shipped in the MiniMed 670G. <sub>`clinical` · PID · state estimation</sub>

**[back to top](#contents)**

### Anesthesia & critical care

1. **[Computer-assisted Individualized Hemodynamic Management Reduces Intraoperative Hypotension in Intermediate- and High-risk Surgery: A Randomized Controlled Trial](https://doi.org/10.1097/aln.0000000000003807)** · Université Paris-Saclay, UC Irvine · 2021 · *paper*  
   Randomized trial where a closed-loop norepinephrine controller held blood pressure near baseline, cutting intraoperative hypotension from 21.5% to 1.2% of case time versus manual titration. <sub>`clinical` · rule-based logic</sub>
2. **[Anesthetic Management Using Multiple Closed-loop Systems and Delayed Neurocognitive Recovery](https://doi.org/10.1097/aln.0000000000003014)** · Université Libre de Bruxelles, UC Irvine · 2020 · *paper*  
   Randomized trial in older surgical patients running three independent closed loops for anesthetic depth, hemodynamic fluids, and ventilation at once, with better one-week cognitive scores. <sub>`clinical` · PID · rule-based logic</sub>
3. **[Fully automated postoperative ventilation in cardiac surgery patients: a randomised clinical trial](https://doi.org/10.1016/j.bja.2020.06.037)** · Catharina Hospital Eindhoven, Amsterdam UMC · 2020 · *paper*  
   POSITiVE trial of 220 post-cardiac-surgery patients on closed-loop INTELLiVENT-ASV, gaining far more time in lung-protective settings and fewer hypoxaemia episodes than conventional ventilation. <sub>`clinical` · optimal control · rule-based logic</sub>
4. **[Closed-loop assisted versus manual goal-directed fluid therapy during high-risk abdominal surgery: a case–control study with propensity matching](https://doi.org/10.1186/s13054-015-0827-7)** · UC Irvine, Hospices Civils de Lyon · 2015 · *paper*  
   Propensity-matched surgical study where a closed-loop fluid controller targeting stroke volume variation kept patients preload-independent about 95% of case time versus 87% with manual care. <sub>`clinical` · rule-based logic</sub>
5. **[Closed-Loop Automatic Oxygen Control (CLAC) in Preterm Infants: A Randomized Controlled Trial](https://doi.org/10.1542/peds.2013-1834)** · University of Tübingen, TU Wien · 2014 · *paper*  
   Crossover trial in 34 ventilated preterm infants where automatic FiO2 titration from pulse oximetry held saturation in target longer and needed fewer manual adjustments than nurses. <sub>`clinical` · rule-based logic</sub>
6. **[Design and Clinical Evaluation of Robust PID Control of Propofol Anesthesia in Children](https://doi.org/10.1109/tcst.2013.2260543)** · University of British Columbia, Lund University · 2014 · *paper*  
   UBC iControl work tuning a PID propofol controller for robustness across identified pediatric patient models, then running it closed-loop on EEG-derived depth of hypnosis in children. <sub>`clinical` · PID · robust control · system identification</sub>
7. **[Evaluation of a novel closed-loop total intravenous anaesthesia drug delivery system: a randomized controlled trial](https://doi.org/10.1093/bja/aet001)** · McGill University · 2013 · *paper*  
   Randomized trial of 186 surgical patients where McGill's McSleepy system dosed propofol, remifentanil and rocuronium from BIS and Analgoscore feedback, beating manual control on hypnosis and analgesia targets. <sub>`clinical` · PID</sub>
8. **[Feasibility study on full closed-loop control ventilation (IntelliVent-ASV™) in ICU patients with acute respiratory failure: a prospective observational comparative study](https://doi.org/10.1186/cc12890)** · Hamilton Medical, Hôpital Sainte Musse · 2013 · *paper*  
   Prospective ICU study of 100 patients ventilated with Hamilton's INTELLiVENT-ASV, which adjusts minute ventilation, PEEP and FiO2 from end-tidal CO2 and SpO2, finding it safe across lung conditions. <sub>`clinical` · optimal control · rule-based logic</sub>
9. **[Closed-Loop Coadministration of Propofol and Remifentanil Guided by Bispectral Index: A Randomized Multicenter Study](https://doi.org/10.1213/ane.0b013e318205680b)** · Hôpital Foch · 2011 · *paper*  
   Multicenter randomized trial of a dual PID loop titrating propofol and remifentanil from the BIS depth-of-anesthesia index, outperforming manual target-controlled infusion in surgical patients. <sub>`clinical` · PID</sub>

**[back to top](#contents)**

### Neuromodulation & cardiac devices

1. **[Long-Term Personalized Adaptive Deep Brain Stimulation in Parkinson Disease](https://doi.org/10.1001/jamaneurol.2025.2781)** · Medtronic, Stanford · 2025 · *paper*  
   ADAPT-PD pivotal trial of Medtronic's single- and dual-threshold sensing-based adaptive DBS in 68 patients at home, the evidence behind BrainSense Adaptive approval. <sub>`clinical` · closed-loop neuromodulation</sub>
2. **[Medtronic earns U.S. FDA approval for the world's first Adaptive deep brain stimulation system for people with Parkinson's](https://news.medtronic.com/2025-02-24-Medtronic-earns-U-S-FDA-approval-for-the-worlds-first-Adaptive-deep-brain-stimulation-system-for-people-with-Parkinsons)** · Medtronic · 2025 · *blog*  
   Announcement of FDA approval of BrainSense Adaptive DBS on Percept neurostimulators, which adjusts stimulation in real time from sensed brain activity in Parkinson's patients. <sub>`production` · closed-loop neuromodulation</sub>
3. **[Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial](https://doi.org/10.1038/s41591-024-03196-z)** · UC San Francisco · 2024 · *paper*  
   Blinded crossover pilot where data-driven neural biomarkers, notably stimulation-entrained gamma, drove chronic adaptive DBS, improving motor symptoms and quality of life over tuned continuous stimulation. <sub>`clinical` · closed-loop neuromodulation · learning-based control</sub>
4. **[Cardiac pacing in severe recurrent reflex syncope and tilt-induced asystole](https://doi.org/10.1093/eurheartj/ehaa936)** · Biotronik, Ospedali del Tigullio · 2021 · *paper*  
   BIOSYNC CLS trial of dual-chamber pacemakers with closed-loop stimulation, which raises rate from sensed intracardiac impedance changes, cutting syncope recurrence from 53% to 16%. <sub>`clinical` · rate-adaptive pacing</sub>
5. **[Long-term safety and efficacy of closed-loop spinal cord stimulation to treat chronic back and leg pain (Evoke): a double-blind, randomised, controlled trial](https://doi.org/10.1016/S1474-4422(19)30414-4)** · Saluda Medical, Cleveland Clinic · 2020 · *paper*  
   Double-blind trial of spinal cord stimulation that tunes current every pulse from recorded evoked compound action potentials, outperforming open-loop stimulation for chronic back and leg pain. <sub>`clinical` · closed-loop neuromodulation</sub>
6. **[Adaptive deep brain stimulation in advanced Parkinson disease](https://doi.org/10.1002/ana.23951)** · University of Oxford, UCL · 2013 · *paper*  
   Acute patient study gating subthalamic stimulation on threshold crossings of local beta-band activity, improving motor scores over continuous DBS while delivering less stimulation. <sub>`clinical` · closed-loop neuromodulation</sub>
7. **[Responsive cortical stimulation for the treatment of medically intractable partial epilepsy](https://doi.org/10.1212/wnl.0b013e3182302056)** · NeuroPace · 2011 · *paper*  
   Pivotal randomized trial of the NeuroPace RNS implant, which detects seizure onset in intracranial EEG and fires responsive stimulation, cutting seizures and leading to FDA approval. <sub>`clinical` · closed-loop neuromodulation</sub>

**[back to top](#contents)**

### Prosthetics & rehabilitation

1. **[A lightweight robotic leg prosthesis replicating the biomechanics of the knee, ankle, and toe joint](https://doi.org/10.1126/scirobotics.abo3996)** · University of Utah · 2022 · *paper*  
   Utah bionic leg combining torque-sensitive knee actuation with an underactuated ankle-toe drive, giving near-normative gait kinetics in three above-knee amputees at prosthesis weight. <sub>`clinical` · impedance control</sub>
2. **[Robotic Leg Control with EMG Decoding in an Amputee with Nerve Transfers](https://doi.org/10.1056/nejmoa1300126)** · Rehabilitation Institute of Chicago · 2013 · *paper*  
   Powered knee-ankle prosthesis whose impedance-controlled ambulation modes were selected by pattern-recognition decoding of reinnervated thigh EMG plus mechanical sensors, tested by a knee-disarticulation amputee across terrains. <sub>`clinical` · impedance control · learning-based control</sub>
3. **[Powered Ankle--Foot Prosthesis Improves Walking Metabolic Economy](https://doi.org/10.1109/tro.2008.2008747)** · MIT · 2009 · *paper*  
   MIT powered ankle, precursor of the commercial BiOM, using series-elastic force control to add push-off work, cutting walking metabolic cost about 14% in three transtibial amputees. <sub>`clinical` · impedance control</sub>

**[back to top](#contents)**

### Agriculture

1. **[Cherry Tomato Production in Intelligent Greenhouses—Sensors and AI for Control of Climate, Irrigation, Crop Yield, and Quality](https://doi.org/10.3390/s20226430)** · Wageningen University & Research · 2020 · *paper*  
   Autonomous Greenhouse Challenge where five teams remotely set climate and irrigation setpoints by AI for six months in real compartments, all outperforming a grower-run reference compartment. <sub>`field` · learning-based control</sub>
2. **[Learning in Centralized Nonlinear Model Predictive Control: Application to an Autonomous Tractor-Trailer System](https://doi.org/10.1109/tcst.2014.2321514)** · KU Leuven, Nanyang Technological University · 2015 · *paper*  
   Nonlinear MPC with moving-horizon state and parameter estimation steering an experimental tractor-trailer, tracking straight lines to centimeter-level error for precision field tasks like weeding and spraying. <sub>`field` · nonlinear MPC · state estimation</sub>
3. **[Automatic Steering of Farm Vehicles Using GPS](https://doi.org/10.2134/1996.precisionagproc3.c91)** · Stanford · 1996 · *paper*  
   Classic field demonstration of carrier-phase GPS autosteer on a large tractor, reaching about 2.5 cm line-tracking accuracy, the approach behind commercial auto-guidance products. <sub>`field` · LQR/LQG</sub>

**[back to top](#contents)**

## Resources

Cross-cutting material. Surveys of control in industry, open-source software with documented deployments, practitioner talks, and books.

### Industry surveys & impact reports

1. **[Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes](https://arxiv.org/abs/2408.03539)** · UT Austin, University of Virginia, Sony AI · 2024 · *paper*  
   Reviews deep RL results achieved on physical robots across core skills and analyzes which factors made those real-world deployments work and what gaps remain. <sub>`operations` · reinforcement learning · learning-based control</sub>
2. **[Control for Societal-scale Challenges: Road Map 2030](https://ieeecss.org/control-societal-scale-challenges-road-map-2030)** · IEEE CSS, MIT, KTH, University of Pennsylvania · 2023 · *report*  
   IEEE CSS roadmap on how control can address climate, healthcare, infrastructure and resilience needs, with chapters on validation, translation to practice, ethics and education. <sub>`operations` · general · learning-based control</sub>
3. **[Challenges of real-world reinforcement learning: definitions, benchmarks and analysis](https://doi.org/10.1007/s10994-021-05961-4)** · Google, Google DeepMind · 2021 · *paper*  
   Google researchers define the obstacles that keep reinforcement learning off physical systems, such as safety constraints, delays and scarce data, and release benchmarks targeting them. <sub>`operations` · reinforcement learning</sub>
4. **[Industry engagement with control research: Perspective and messages](https://doi.org/10.1016/j.arcontrol.2020.03.002)** · University of Minnesota, MERL, Politecnico di Milano, IFAC · 2020 · *paper*  
   IFAC Industry Committee members from firms such as ASML, Airbus and Medtronic report a survey of control technology impact and give ten messages for researchers. <sub>`operations` · general · PID · MPC</sub>
5. **[Learning-Based Model Predictive Control: Toward Safe Learning in Control](https://doi.org/10.1146/annurev-control-090419-075625)** · ETH Zurich · 2020 · *paper*  
   ETH Zurich review of MPC schemes that learn dynamics, costs or safety certificates from data, emphasizing how safety can be retained when applied to real systems. <sub>`operations` · MPC · learning-based control</sub>
6. **[Real-time optimization and model predictive control for aerospace and automotive applications](https://doi.org/10.23919/ACC.2018.8431585)** · MERL, University of Michigan · 2018 · *paper*  
   ACC tutorial by MERL and Michigan authors reviewing how real-time optimization and MPC have been developed and applied for automotive and aerospace systems. <sub>`operations` · MPC · convex optimization · trajectory optimization</sub>
7. **[A Survey on Industry Impact and Challenges Thereof](https://doi.org/10.1109/MCS.2016.2621438)** · University of Minnesota, IFAC · 2017 · *paper*  
   IEEE Control Systems Magazine column introducing IFAC's pilot Industry Committee and its effort to gauge the industrial impact of control technologies and the obstacles to it. <sub>`operations` · general</sub>
8. **[Embedded Optimization Methods for Industrial Automatic Control](https://doi.org/10.1016/j.ifacol.2017.08.1946)** · ABB, University of Freiburg, ETH Zurich, embotech, EPFL · 2017 · *paper*  
   ABB, embotech and academic authors survey embedded solvers for real-time MPC and estimation, citing industrial uses in engines, power electronics, cranes and LHC cryogenics. <sub>`operations` · MPC · convex optimization · nonlinear MPC</sub>
9. **[The current state of control loop performance monitoring – A survey of application in industry](https://doi.org/10.1016/j.jprocont.2015.11.002)** · ABB, Zhejiang University, TH Köln, Imperial College London · 2016 · *paper*  
   ABB-led survey of how control-loop performance monitoring is applied in industry, which techniques are in use and which problems remain open. <sub>`operations` · PID · general</sub>
10. **[Model Predictive Control in Industry: Challenges and Opportunities](https://doi.org/10.1016/j.ifacol.2015.09.022)** · Honeywell, Saudi Aramco, University of British Columbia · 2015 · *paper*  
   Honeywell and Saudi Aramco engineers, with a UBC coauthor, outline the challenges industrial MPC faces in practice and the opportunities they open for research. <sub>`operations` · MPC · system identification</sub>
11. **[The Impact of Control Technology, 2nd Edition](https://www.ieeecss.org/impact-control-technology-2nd-edition)** · IEEE CSS · 2014 · *report*  
   Updated IEEE CSS collection of 30 industrial success stories, such as PID auto-tuners, mobile phones, UAV autopilots and Formula One, plus 38 research challenge flyers. <sub>`operations` · general</sub>
12. **[The development of Model Predictive Control in automotive industry: A survey](https://doi.org/10.1109/CCA.2012.6402735)** · Ford, MERL, University of Michigan · 2012 · *paper*  
   Ford researchers and collaborators survey how MPC has been developed and applied for automotive systems such as powertrain and vehicle dynamics control. <sub>`operations` · MPC</sub>
13. **[The Impact of Control Technology: Overview, Success Stories, and Research Challenges](https://www.ieeecss.org/impact-control-technology-1st-edition)** · IEEE CSS · 2011 · *report*  
   IEEE CSS report gathering short success stories of deployed control and open research challenges across aerospace, automotive, process, energy and other industries. <sub>`operations` · general</sub>
14. **[A survey of industrial model predictive control technology](https://doi.org/10.1016/S0967-0661(02)00186-7)** · UT Austin, AspenTech · 2003 · *paper*  
   Landmark review of commercial MPC vendor products and their application counts by industry, comparing how linear and nonlinear packages handle modeling, identification and optimization. <sub>`operations` · MPC · nonlinear MPC · system identification</sub>
15. **[Increasing Customer Value of Industrial Control Performance Monitoring—Honeywell's Experience](https://skoge.folk.ntnu.no/prost/proceedings/cpc6-jan2002/desborough.pdf)** · Honeywell · 2002 · *paper*  
   Honeywell field data show about 97% of regulatory loops in refining, chemicals and pulp and paper use PID, and only about a third perform acceptably. <sub>`operations` · PID</sub>
16. **[The future of PID control](https://doi.org/10.1016/S0967-0661(01)00062-4)** · Lund University · 2001 · *paper*  
   Åström and Hägglund examine why PID still dominates industrial loops and how tuning, auto-tuning, implementation details and design tools should evolve. <sub>`operations` · PID</sub>

**[back to top](#contents)**

### Software with documented deployments

1. **[ros2_control](https://control.ros.org/)** · ros-controls, OSRA · 2020 · *code*  
   Real-time ROS 2 control framework with manufacturer-supported drivers from Universal Robots, Fanuc, Franka, Kinova and Denso for running controllers on industrial arms. <sub>`production` · PID · general</sub>
2. **[ROSCO: Reference Open-Source Controller](https://github.com/NREL/ROSCO)** · NREL · 2020 · *code*  
   NREL's industry-representative wind turbine controller, the baseline for IEA 3.4, 10 and 15 MW reference turbines and tested in 1:70-scale floating-turbine basin experiments. <sub>`production` · PID · gain scheduling</sub>
3. **[acados](https://github.com/acados/acados)** · University of Freiburg · 2019 · *code*  
   Embedded C solvers for nonlinear MPC and moving horizon estimation, used in comma.ai's openpilot driver assistance, wind-turbine control studies and real quadrotor flight. <sub>`production` · nonlinear MPC · state estimation · optimal control</sub>
4. **[OSQP](https://osqp.org/)** · University of Oxford, Stanford, Princeton University, IMT Lucca, ETH Zurich · 2017 · *code*  
   ADMM-based QP solver that can generate library-free embedded C code for MPC, listing Toyota, Siemens, Aptiv and Lyft among its users. <sub>`production` · convex optimization · MPC</sub>
5. **[openpilot](https://github.com/commaai/openpilot)** · comma.ai · 2016 · *code*  
   comma.ai's open-source driver assistance system for 300+ supported cars. Its planners historically ran acados-solved MPC, and later releases replaced lateral and experimental longitudinal MPC with learned end-to-end policies. <sub>`production` · MPC · learning-based control</sub>
6. **[FORCESPRO](https://embotech.ai/forcespro)** · embotech · 2014 · *code*  
   Commercial generator of embedded MPC solvers from embotech, aimed at automotive planning, industrial automation and aerospace, and usable through MathWorks' MPC Toolbox. <sub>`production` · MPC · nonlinear MPC · convex optimization</sub>
7. **[CVXGEN: a code generator for embedded convex optimization](https://doi.org/10.1007/s11081-011-9176-9)** · Stanford · 2012 · *paper*  
   Describes CVXGEN, which emits fast custom C solvers for small QPs; SpaceX uses it to generate onboard convex optimization code for Falcon 9 landing. <sub>`production` · convex optimization · MPC · trajectory optimization</sub>
8. **[PX4 Autopilot](https://github.com/PX4/PX4-Autopilot)** · Dronecode Foundation · 2012 · *code*  
   BSD-licensed flight stack under the Linux Foundation's Dronecode project, flying commercial multirotor, fixed-wing, VTOL, cargo and survey vehicles plus rovers and submersibles. <sub>`production` · PID · Kalman filtering · state estimation</sub>
9. **[CasADi](https://web.casadi.org/)** · KU Leuven · 2011 · *code*  
   Algorithmic differentiation and optimal control framework used by acados for model specification and as the backend of tools such as JModelica.org and Deltares' RTC-Tools. <sub>`production` · optimal control · nonlinear MPC · trajectory optimization</sub>
10. **[ArduPilot](https://github.com/ArduPilot/ardupilot)** · ArduPilot Project · 2009 · *code*  
   GPL autopilot for planes, copters, helicopters, rovers, boats and subs, installed in over a million vehicles, used by companies, universities and agencies like NASA, and run on the 3DR Solo. <sub>`production` · PID · Kalman filtering</sub>
11. **[qpOASES](https://github.com/coin-or/qpOASES)** · Heidelberg University, ABB · 2007 · *code*  
   Online active-set QP solver designed for MPC, code-generated onto an industrial PLC in NTNU and ABB hardware-in-the-loop tests using Statoil SEPTIC controller configurations. <sub>`production` · MPC · convex optimization</sub>

**[back to top](#contents)**

### Talks & videos

1. **[Applying Spot to Real World Applications](https://www.youtube.com/watch?v=_V_ApampCDQ)** · Boston Dynamics · 2021 · *talk*  
   Spot engineering lead Marco da Silva describes how Boston Dynamics turned its quadruped into an industrial sensing platform via an extensible API, autonomy features and payload support. <sub>`operations` · general</sub>
2. **[Recent Progress on Atlas, the World's Most Dynamic Humanoid Robot](https://www.youtube.com/watch?v=EGABAx52GKI)** · Boston Dynamics · 2020 · *talk*  
   Boston Dynamics' Scott Kuindersma explains how optimization lets the Atlas team rapidly create dynamic humanoid behaviors, including perception-driven parkour, in a Robotics Today seminar. <sub>`operations` · trajectory optimization · optimal control</sub>
3. **[Control Systems in Practice](https://www.mathworks.com/videos/series/control-systems-in-practice.html)** · MathWorks · 2018 · *video*  
   Brian Douglas's MathWorks video series on the practical side of control engineering, including the job beyond tuning, gain scheduling, feedforward, time delays and coding transfer functions. <sub>`operations` · gain scheduling · feedforward · PID</sub>
4. **[Understanding Model Predictive Control](https://www.mathworks.com/videos/series/understanding-model-predictive-control.html)** · MathWorks · 2018 · *video*  
   MathWorks series introducing MPC design parameters and variants, then designing nonlinear MPC with FORCESPRO and running it on Speedgoat real-time hardware. <sub>`operations` · MPC · nonlinear MPC</sub>
5. **[Understanding PID Control](https://www.mathworks.com/videos/series/understanding-pid-control.html)** · MathWorks · 2018 · *video*  
   Seven short MathWorks videos by Brian Douglas covering implementation issues such as integrator windup, derivative filtering, plant modeling and manual versus automatic PID tuning. <sub>`operations` · PID</sub>
6. **[Meet Spot, the robot dog that can run, hop and open doors](https://www.ted.com/talks/marc_raibert_meet_spot_the_robot_dog_that_can_run_hop_and_open_doors)** · Boston Dynamics · 2017 · *talk*  
   Boston Dynamics founder Marc Raibert presents the company's dynamically balanced legged machines and demonstrates SpotMini mapping, climbing stairs and manipulating objects live on stage. <sub>`operations` · general</sub>

**[back to top](#contents)**

### Books & long-form guides

1. **[Feedback Systems: An Introduction for Scientists and Engineers](https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers)** · Lund University, Caltech · 2021 · *book*  
   Åström and Murray's freely downloadable second edition covering modeling, feedback principles, PID, state feedback, frequency-domain design and robustness, with examples across engineering domains. <sub>`operations` · PID · LQR/LQG · robust control · general</sub>
2. **[Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control](https://databookuw.com/)** · University of Washington · 2019 · *book*  
   Brunton and Kutz connect machine learning with system identification and data-driven control, with downloadable MATLAB and Python code and data on the companion site. <sub>`operations` · system identification · learning-based control · reinforcement learning</sub>
3. **[Model Predictive Control: Theory, Computation, and Design](https://sites.engineering.ucsb.edu/~jbraw/mpc/)** · UCSB, Imperial College London, University of Freiburg · 2017 · *book*  
   Rawlings, Mayne and Diehl's second edition, available as free PDF, covering MPC stability theory, moving horizon estimation and the numerical optimization behind practical implementations. <sub>`operations` · MPC · state estimation · nonlinear MPC</sub>
4. **[Control Performance Management in Industrial Automation: Assessment, Diagnosis and Improvement of Control Loop Performance](https://link.springer.com/book/10.1007/978-1-4471-4546-2)** · TH Köln · 2013 · *book*  
   Monograph on assessing loop performance, diagnosing oscillations, nonlinearities and actuator faults, and retuning controllers, illustrated with case studies from chemicals, mining and paper mills. <sub>`operations` · PID · general</sub>
5. **[Feedback Control for Computer Systems](https://www.oreilly.com/library/view/feedback-control-for/9781449362638/)** · Philipp K. Janert · 2013 · *book*  
   Hands-on guide by Philipp Janert applying feedback loops to enterprise software, using simulations of data-center problems such as adding servers automatically during traffic spikes. <sub>`operations` · PID</sub>
6. **[PID Control in the Third Millennium: Lessons Learned and New Approaches](https://link.springer.com/book/10.1007/978-1-4471-2425-2)** · Universitat Autònoma de Barcelona, University of Brescia · 2012 · *book*  
   Edited Springer volume reviewing PID tuning, implementation and data-driven design, including a chapter by practitioner Greg McMillan on industrial PID applications. <sub>`operations` · PID</sub>
7. **[Feedback Control of Computing Systems](https://doi.org/10.1002/047166880X)** · IBM, University of Michigan · 2004 · *book*  
   A textbook from IBM researchers and Dawn Tilbury on modeling computing systems and designing feedback controllers for them, from system identification through PID and state-space design. <sub>`operations` · PID · system identification · LQR/LQG</sub>
8. **[Simple analytic rules for model reduction and PID controller tuning](https://doi.org/10.1016/S0959-1524(02)00062-8)** · NTNU · 2003 · *paper*  
   Skogestad's SIMC method for reducing plant models and tuning PI and PID loops in a single step, a widely used reference for process-industry tuning. <sub>`operations` · PID</sub>

**[back to top](#contents)**

## Browse by method

The same deployments, regrouped by the control method they rely on. Full lists are in [docs/by-method.md](docs/by-method.md).

| Method | Entries | Description |
|---|---:|---|
| [MPC](docs/by-method.md#mpc) | 54 | Model predictive control with online optimization |
| [PID](docs/by-method.md#pid) | 41 | Proportional-integral-derivative feedback and its variants |
| [state estimation](docs/by-method.md#state-estimation) | 37 | Observers, moving-horizon estimation, and sensor fusion |
| [reinforcement learning](docs/by-method.md#reinforcement-learning) | 30 | Policies learned from interaction, in simulation or on hardware |
| [adaptive control](docs/by-method.md#adaptive-control) | 20 | Online adaptation of controller parameters (MRAC, L1, self-tuning) |
| [system identification](docs/by-method.md#system-identification) | 18 | Building control-oriented models from data |
| [learning-based control](docs/by-method.md#learning-based-control) | 17 | Data-driven models or controllers short of full RL |
| [distributed control](docs/by-method.md#distributed-control) | 16 | Multi-agent, decentralized, or networked control |
| [feedforward](docs/by-method.md#feedforward) | 16 | Model-based or measured-disturbance feedforward |
| [Kalman filtering](docs/by-method.md#kalman-filtering) | 16 | Kalman, extended, and unscented filters |
| [convex optimization](docs/by-method.md#convex-optimization) | 15 | Guidance or control posed as a convex program solved onboard or online |
| [optimal control](docs/by-method.md#optimal-control) | 13 | Pontryagin, calculus of variations, and related optimal control |
| [trajectory optimization](docs/by-method.md#trajectory-optimization) | 12 | Offline or online computation of open-loop or reference trajectories |
| [gain scheduling](docs/by-method.md#gain-scheduling) | 11 | Controllers interpolated across operating points |
| [general](docs/by-method.md#general) | 11 | Broad coverage of control methods |
| [nonlinear MPC](docs/by-method.md#nonlinear-mpc) | 11 | MPC with nonlinear prediction models |
| [queueing control](docs/by-method.md#queueing-control) | 10 | Feedback on queue length, delay, or concurrency |
| [feedback control](docs/by-method.md#feedback-control) | 9 | Engineered feedback loops described without a named design method |
| [LQR/LQG](docs/by-method.md#lqrlqg) | 8 | Linear-quadratic regulation and Gaussian estimation |
| [rule-based logic](docs/by-method.md#rule-based-logic) | 8 | Hand-designed threshold and decision logic |
| [fault-tolerant control](docs/by-method.md#fault-tolerant-control) | 7 | Reconfiguration and accommodation of failures |
| [impedance control](docs/by-method.md#impedance-control) | 7 | Impedance, admittance, and force control for physical interaction |
| [closed-loop neuromodulation](docs/by-method.md#closed-loop-neuromodulation) | 6 | Stimulation adjusted by sensed neural biomarkers |
| [setpoint optimization](docs/by-method.md#setpoint-optimization) | 6 | Choosing operating setpoints (for example yaw offsets) to optimize a plant-level objective |
| [whole-body control](docs/by-method.md#whole-body-control) | 6 | Task-space control of floating-base robots via prioritized optimization |
| [AIMD](docs/by-method.md#aimd) | 5 | Additive-increase multiplicative-decrease feedback |
| [droop control](docs/by-method.md#droop-control) | 5 | Proportional power-frequency or power-voltage sharing among sources |
| [dynamic inversion](docs/by-method.md#dynamic-inversion) | 5 | Nonlinear dynamic inversion and feedback linearization |
| [dynamic programming](docs/by-method.md#dynamic-programming) | 5 | Bellman recursion, value iteration, and approximate DP |
| [robust control](docs/by-method.md#robust-control) | 5 | H-infinity, mu-synthesis, loop shaping, and related robust designs |
| [imitation learning](docs/by-method.md#imitation-learning) | 4 | Policies learned from demonstrations |
| [real-time optimization](docs/by-method.md#real-time-optimization) | 4 | Steady-state economic optimization layered above regulatory control |
| [run-to-run control](docs/by-method.md#run-to-run-control) | 3 | Batch-to-batch feedback in semiconductor and batch processes |
| [event-triggered control](docs/by-method.md#event-triggered-control) | 2 | Updates triggered by state or error conditions |
| [fuzzy logic](docs/by-method.md#fuzzy-logic) | 2 | Fuzzy rule-based control |
| [grid-forming control](docs/by-method.md#grid-forming-control) | 2 | Inverters that set grid voltage and frequency rather than follow them |
| [iterative learning control](docs/by-method.md#iterative-learning-control) | 2 | Trial-to-trial learning for repetitive tasks |
| [teleoperation](docs/by-method.md#teleoperation) | 2 | Human-in-the-loop remote control with force or motion feedback |
| [wide-area control](docs/by-method.md#wide-area-control) | 2 | Grid-scale control using synchronized phasor measurements |
| [behavior-based control](docs/by-method.md#behavior-based-control) | 1 | Layered reactive behaviors arbitrated without a global model |
| [expert systems](docs/by-method.md#expert-systems) | 1 | Rule-based supervisory control encoding operator knowledge |
| [predictor-corrector guidance](docs/by-method.md#predictor-corrector-guidance) | 1 | Guidance that repeatedly predicts the trajectory and corrects commands toward a target |
| [rate-adaptive pacing](docs/by-method.md#rate-adaptive-pacing) | 1 | Cardiac pacing rate adjusted from sensed physiological signals |
| [sliding mode](docs/by-method.md#sliding-mode) | 1 | Variable-structure and sliding-mode control |
| [stochastic optimization](docs/by-method.md#stochastic-optimization) | 1 | Decisions optimized against forecast uncertainty or risk |
| [trajectory prediction](docs/by-method.md#trajectory-prediction) | 1 | Forward simulation of candidate maneuvers to decide when or how to intervene |
| [transactive control](docs/by-method.md#transactive-control) | 1 | Market or price signals used to coordinate distributed loads |
| [virtual fixtures](docs/by-method.md#virtual-fixtures) | 1 | Haptic constraints that guide or bound a human-operated tool |
| [visual servoing](docs/by-method.md#visual-servoing) | 1 | Feedback driven directly by camera measurements |
| [ZMP control](docs/by-method.md#zmp-control) | 1 | Balance control that regulates the zero-moment point of a legged robot |

## Related lists

- [eugeneyan/applied-ml](https://github.com/eugeneyan/applied-ml): the model for this list, covering machine learning in production.
- [A-make/awesome-control-theory](https://github.com/A-make/awesome-control-theory): resources for learning control theory.
- [jkoendev/optimal-control-literature-software](https://github.com/jkoendev/optimal-control-literature-software): literature and software for optimal control and MPC.
- [robotsorcerer/awesome-neurocontrol](https://github.com/robotsorcerer/awesome-neurocontrol): neural network methods in control.

## Contributing

Additions and corrections are welcome. Entries live as YAML in [`data/`](data/), and the README
is generated from them. See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion criteria, the
entry format, and how to run the validator.

## License

[MIT](LICENSE). Linked works belong to their respective authors and publishers. Summaries are
original paraphrases written for this list.

<sub>This README is generated from the files in [`data/`](data/) by [`scripts/build.py`](scripts/build.py). Edit the data, not this file.</sub>
