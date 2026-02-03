"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { useTheme } from "next-themes";
import {
  FileText,
  Download,
  MapPin,
  Users,
  Home,
  Shield,
  Clock,
  AlertTriangle,
  CheckCircle,
  Search,
  ChevronDown,
  ChevronUp,
  Phone,
  Mail,
  Calendar,
  DollarSign,
  BookOpen,
  Eye,
  UserCheck,
  Ban,
  Zap,
  Heart,
  Coffee,
  Wifi,
  Car,
  Utensils,
  Dumbbell,
  Book,
  Tv,
  Shirt,
  Stethoscope,
} from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "../ui/card";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { Badge } from "../ui/badge";

const EligibilityContainer = () => {
  const { resolvedTheme } = useTheme();
  const isDark = resolvedTheme === "dark";
  const [searchTerm, setSearchTerm] = useState("");
  const [expandedSections, setExpandedSections] = useState({});

  const toggleSection = (sectionId) => {
    setExpandedSections(prev => ({
      ...prev,
      [sectionId]: !prev[sectionId]
    }));
  };

  const handleDownload = () => {
    const link = document.createElement('a');
    link.href = '/folder/Prospectus.pdf';
    link.download = 'TABH-Prospectus.pdf';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
      },
    },
  };

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: {
        duration: 0.5,
      },
    },
  };

  return (
    <div
      className={`min-h-screen w-full p-4 md:p-8 rounded-xl ${
        isDark
          ? "bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900"
          : "bg-gradient-to-br from-vips-cream via-white to-vips-cream"
      }`}
    >
      <motion.div
        className="max-w-7xl mx-auto"
        variants={containerVariants}
        initial="hidden"
        animate="visible"
      >
        {/* Header Section */}
        <motion.div variants={itemVariants} className="mb-8">
          <Card
            className={
              isDark
                ? "bg-black/30 border-white/10 backdrop-blur-md"
                : "bg-white/60 border-black/5 shadow-lg backdrop-blur-md"
            }
          >
            <CardHeader className="text-center">
              <div className="flex items-center justify-center mb-4">
                <div
                  className={`w-16 h-16 rounded-full flex items-center justify-center ${
                    isDark
                      ? "bg-gradient-to-br from-purple-500/30 to-purple-500/10"
                      : "bg-gradient-to-br from-red-500/30 to-red-500/10"
                  }`}
                >
                  <Shield className="text-red-600 h-8 w-8" />
                </div>
              </div>
              <CardTitle
                className={`text-4xl md:text-5xl font-bold mb-4 font-orbitron ${
                  isDark ? "text-white" : "text-gray-800"
                }`}
              >
                <span className="bg-gradient-to-r from-red-600 to-red-800 bg-clip-text text-transparent">
                  TABH Eligibility & Prospectus
                </span>
              </CardTitle>
              <p
                className={`text-lg ${
                  isDark ? "text-gray-300" : "text-gray-600"
                } max-w-3xl mx-auto`}
              >
                Complete information about admission criteria, facilities, rules, and regulations for 
                <strong> Tauras Army Boys Hostel</strong> - Your home away from home in Delhi.
              </p>
              
              {/* Download Button */}
              <div className="mt-6">
                <Button
                  onClick={handleDownload}
                  className="bg-gradient-to-r from-red-600 to-red-700 hover:from-red-700 hover:to-red-800 text-white px-8 py-3 rounded-full font-semibold shadow-lg hover:shadow-xl transition-all duration-300"
                >
                  <Download className="mr-2 h-5 w-5" />
                  Download Complete Prospectus (PDF)
                </Button>
              </div>
            </CardHeader>
          </Card>
        </motion.div>

        {/* Search Bar */}
        <motion.div variants={itemVariants} className="mb-8">
          <div className="relative max-w-md mx-auto">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-5 w-5" />
            <Input
              type="text"
              placeholder="Search eligibility information..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-10 pr-4 py-3 rounded-full border-2 focus:border-red-500"
            />
          </div>
        </motion.div>

        {/* Quick Stats */}
        <motion.div variants={itemVariants} className="mb-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <Card className={isDark ? "bg-black/20 border-white/10" : "bg-white/80 border-black/5"}>
              <CardContent className="p-4 text-center">
                <MapPin className="h-8 w-8 mx-auto mb-2 text-red-600" />
                <p className="text-2xl font-bold text-red-600">Delhi Cantt</p>
                <p className={`text-sm ${isDark ? "text-gray-300" : "text-gray-600"}`}>Location</p>
              </CardContent>
            </Card>
            <Card className={isDark ? "bg-black/20 border-white/10" : "bg-white/80 border-black/5"}>
              <CardContent className="p-4 text-center">
                <Users className="h-8 w-8 mx-auto mb-2 text-blue-600" />
                <p className="text-2xl font-bold text-blue-600">Army Sons</p>
                <p className={`text-sm ${isDark ? "text-gray-300" : "text-gray-600"}`}>Eligible</p>
              </CardContent>
            </Card>
            <Card className={isDark ? "bg-black/20 border-white/10" : "bg-white/80 border-black/5"}>
              <CardContent className="p-4 text-center">
                <Home className="h-8 w-8 mx-auto mb-2 text-green-600" />
                <p className="text-2xl font-bold text-green-600">24/7</p>
                <p className={`text-sm ${isDark ? "text-gray-300" : "text-gray-600"}`}>Security</p>
              </CardContent>
            </Card>
            <Card className={isDark ? "bg-black/20 border-white/10" : "bg-white/80 border-black/5"}>
              <CardContent className="p-4 text-center">
                <Clock className="h-8 w-8 mx-auto mb-2 text-purple-600" />
                <p className="text-2xl font-bold text-purple-600">3 Years</p>
                <p className={`text-sm ${isDark ? "text-gray-300" : "text-gray-600"}`}>Max Stay</p>
              </CardContent>
            </Card>
          </div>
        </motion.div>

        {/* Main Content Sections */}
        <div className="space-y-6">
          {/* Location & General Info */}
          <EligibilitySection
            id="location"
            title="Location & General Information"
            icon={<MapPin className="h-6 w-6" />}
            isDark={isDark}
            expanded={expandedSections.location}
            onToggle={() => toggleSection('location')}
            searchTerm={searchTerm}
          >
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <h4 className="font-semibold mb-3 text-red-600">📍 Hostel Location</h4>
                <ul className="space-y-2 text-sm">
                  <li>• <strong>Address:</strong> Kirki Place (COD Complex), Delhi Cantt</li>
                  <li>• <strong>Near:</strong> Palliative Care Centre</li>
                  <li>• <strong>Concept:</strong> "Home away from home" for army boys pursuing higher education</li>
                </ul>
              </div>
              <div>
                <h4 className="font-semibold mb-3 text-blue-600">🚗 Connectivity</h4>
                <ul className="space-y-2 text-sm">
                  <li>• Well connected with Indira Gandhi International Airport</li>
                  <li>• Close to Palam Airport</li>
                  <li>• Near Delhi Cantt Railway Station</li>
                </ul>
              </div>
            </div>
          </EligibilitySection>

          {/* Eligibility Criteria */}
          <EligibilitySection
            id="eligibility"
            title="Eligibility Criteria & Priority System"
            icon={<UserCheck className="h-6 w-6" />}
            isDark={isDark}
            expanded={expandedSections.eligibility}
            onToggle={() => toggleSection('eligibility')}
            searchTerm={searchTerm}
          >
            <div className="space-y-6">
              <div className="bg-blue-50 dark:bg-blue-900/20 p-4 rounded-lg border-l-4 border-blue-500">
                <h4 className="font-semibold mb-2 text-blue-700 dark:text-blue-300">🎯 Target Group</h4>
                <p className="text-sm">Accommodation available for dependents of all ranks serving/retired and war widows/widowers in Army and NOT having any type of accommodation in Delhi NCR.</p>
              </div>
              
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-semibold mb-3 text-red-600">🥇 Priority I</h4>
                  <ul className="space-y-2 text-sm">
                    <li>• <strong>Battle Casualties & Gallantry Awardees:</strong> Wards of Battle casualties and Gallantry Awardees/Veer Naris pursuing studies of one year or more in Delhi</li>
                    <li>• <strong>Serving Army Personnel:</strong> Wards of Serving Army persons not having accommodation (SF account) in Delhi & posted outside Delhi NCR</li>
                  </ul>
                </div>
                <div>
                  <h4 className="font-semibold mb-3 text-orange-600">🥈 Priority II</h4>
                  <ul className="space-y-2 text-sm">
                    <li>• <strong>NCR Posted:</strong> Son of serving army persons living/posted in Ghaziabad, Noida, Faridabad or Gurgaon pursuing studies of one year or more in Delhi</li>
                    <li>• <strong>Coaching/Training:</strong> Son of serving army persons pursuing any coaching or vocational training of one year or more</li>
                  </ul>
                </div>
              </div>
              
              <div className="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-lg border-l-4 border-yellow-500">
                <h4 className="font-semibold mb-2 text-yellow-700 dark:text-yellow-300">🥉 Priority III</h4>
                <ul className="space-y-2 text-sm">
                  <li>• <strong>Ex-Servicemen Sons:</strong> Sons of ex-servicemen, if vacancies exist, opened after 31 Aug. However, they can register before that and be on waitlist</li>
                  <li>• <strong>Admission Policy:</strong> Initially to one son & admission to second son will only be given if seats are available in the hostel</li>
                </ul>
              </div>
              
              <div className="bg-red-50 dark:bg-red-900/20 p-4 rounded-lg border-l-4 border-red-500">
                <h4 className="font-semibold mb-2 text-red-700 dark:text-red-300">⚠️ Important Notes</h4>
                <ul className="space-y-2 text-sm">
                  <li>• Students undergoing any Course through correspondence or pursuing paid internship are not permitted</li>
                  <li>• Working or job holders or those not pursuing higher education are not permitted to stay in hostel</li>
                  <li>• Admission will be strictly on first come first served basis and subject to proof of admission to course/graduation course</li>
                </ul>
              </div>
            </div>
          </EligibilitySection>

          {/* Facilities Provided */}
          <EligibilitySection
            id="facilities"
            title="Facilities Provided"
            icon={<Home className="h-6 w-6" />}
            isDark={isDark}
            expanded={expandedSections.facilities}
            onToggle={() => toggleSection('facilities')}
            searchTerm={searchTerm}
          >
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div>
                <h4 className="font-semibold mb-3 text-blue-600 flex items-center gap-2">
                  <Home className="h-5 w-5" /> Accommodation
                </h4>
                <ul className="space-y-2 text-sm">
                  <li>• Room with attached bath & store (2 students)</li>
                  <li>• Dormitory for 4 students with common bath room (Rs 1000/- less than room)</li>
                  <li>• Furnished rooms with modern toilets</li>
                  <li>• Geysers for winter bathing</li>
                </ul>
              </div>
              
              <div>
                <h4 className="font-semibold mb-3 text-green-600 flex items-center gap-2">
                  <Utensils className="h-5 w-5" /> Food & Dining
                </h4>
                <ul className="space-y-2 text-sm">
                  <li>• Hygienic meals in clean ambience</li>
                  <li>• AC Dining hall</li>
                  <li>• Hygienic food provided by contractor</li>
                  <li>• 58" Colour LCD with TATA SKY Connection in dining room</li>
                </ul>
              </div>
              
              <div>
                <h4 className="font-semibold mb-3 text-purple-600 flex items-center gap-2">
                  <Dumbbell className="h-5 w-5" /> Recreation & Sports
                </h4>
                <ul className="space-y-2 text-sm">
                  <li>• Multi Station Gym for health benefits</li>
                  <li>• Badminton and chess facility</li>
                  <li>• Recreation room with cable TV</li>
                  <li>• Two lawns/gardens for relaxation</li>
                </ul>
              </div>
              
              <div>
                <h4 className="font-semibold mb-3 text-orange-600 flex items-center gap-2">
                  <Book className="h-5 w-5" /> Study & Learning
                </h4>
                <ul className="space-y-2 text-sm">
                  <li>• Library with sufficient number of books</li>
                  <li>• Daily newspapers and magazines in common room</li>
                  <li>• Study chair & table in each room</li>
                  <li>• Desert cooler in all rooms</li>
                </ul>
              </div>
              
              <div>
                <h4 className="font-semibold mb-3 text-cyan-600 flex items-center gap-2">
                  <Shirt className="h-5 w-5" /> Services
                </h4>
                <ul className="space-y-2 text-sm">
                  <li>• Free Laundry services</li>
                  <li>• Modern laundry service</li>
                  <li>• Round the clock security</li>
                  <li>• Civil & Military telephone</li>
                </ul>
              </div>
              
              <div>
                <h4 className="font-semibold mb-3 text-red-600 flex items-center gap-2">
                  <Stethoscope className="h-5 w-5" /> Health & Safety
                </h4>
                <ul className="space-y-2 text-sm">
                  <li>• First Aid available 24 hours</li>
                  <li>• RO Water purification system with water cooler in every building</li>
                  <li>• Medical fitness certificate required</li>
                  <li>• Required immunizations supported by certificate</li>
                </ul>
              </div>
            </div>
          </EligibilitySection>

          {/* Fees and Charges */}
          <EligibilitySection
            id="fees"
            title="Fees and Charges"
            icon={<DollarSign className="h-6 w-6" />}
            isDark={isDark}
            expanded={expandedSections.fees}
            onToggle={() => toggleSection('fees')}
            searchTerm={searchTerm}
          >
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <h4 className="font-semibold mb-3 text-green-600">💰 One-Time Fees</h4>
                <ul className="space-y-2 text-sm">
                  <li>• <strong>Registration:</strong> One-time non-refundable fee (to be paid along with registration form)</li>
                  <li>• <strong>Admission Fee:</strong> One-time fee at admission (non-refundable)</li>
                  <li>• <strong>Caution/Security Money:</strong> Paid at admission and is refundable</li>
                  <li>• <strong>Hostel Identity Card:</strong> Rs 20/- (non-refundable), Rs 100/- for duplicate</li>
                </ul>
              </div>
              
              <div>
                <h4 className="font-semibold mb-3 text-blue-600">📅 Monthly Charges</h4>
                <ul className="space-y-2 text-sm">
                  <li>• <strong>Allied Charges:</strong> Monthly payment irrespective of number of days stayed</li>
                  <li>• <strong>Messing Charges:</strong> Contract agreement with outsourced contractor</li>
                  <li>• <strong>Advance Payment:</strong> Monthly subscription required to be submitted latest by 7th of each month</li>
                  <li>• <strong>Late Fee:</strong> Rs 20/- per day after stipulated date</li>
                </ul>
              </div>
              
              <div className="md:col-span-2">
                <div className="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-lg border-l-4 border-yellow-500">
                  <h4 className="font-semibold mb-2 text-yellow-700 dark:text-yellow-300">💳 Payment Information</h4>
                  <ul className="space-y-2 text-sm">
                    <li>• All payments will only be made through POS machines installed at the hostel</li>
                    <li>• Messing will be refunded during absent period for 03 or more days</li>
                    <li>• If a ward vacates the hostel prior to 15 days, Allied charges will be charged for 15 days</li>
                    <li>• Any recoveries on account of damage/deficient property will be made good from security money</li>
                  </ul>
                </div>
              </div>
            </div>
          </EligibilitySection>

          {/* Rules and Regulations */}
          <EligibilitySection
            id="rules"
            title="Hostel Rules & Regulations"
            icon={<AlertTriangle className="h-6 w-6" />}
            isDark={isDark}
            expanded={expandedSections.rules}
            onToggle={() => toggleSection('rules')}
            searchTerm={searchTerm}
          >
            <div className="space-y-6">
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-semibold mb-3 text-red-600">🚫 Prohibited Items & Activities</h4>
                  <ul className="space-y-2 text-sm">
                    <li>• Tobacco items, alcohol, liquor, banned drugs strictly prohibited</li>
                    <li>• Electric iron, heater, and immersion rod prohibited</li>
                    <li>• Ragging is strictly prohibited - violators will be expelled</li>
                    <li>• No fire arms allowed in hostel</li>
                    <li>• Cooking of food in rooms is prohibited</li>
                    <li>• No pets allowed in hostel</li>
                    <li>• No guests permitted to stay in hostel</li>
                  </ul>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-3 text-blue-600">⏰ Time Restrictions</h4>
                  <ul className="space-y-2 text-sm">
                    <li>• <strong>Lights Out:</strong> 2330hrs (individual table lamps allowed for study)</li>
                    <li>• <strong>Main Gate:</strong> Closed at 2200h, opened at 0600h by JCO Warden</li>
                    <li>• <strong>Late Return:</strong> Rs 200/- penalty per day for late coming</li>
                    <li>• <strong>Night-out Pass:</strong> Written request 48hrs in advance</li>
                  </ul>
                </div>
              </div>
              
              <div className="bg-red-50 dark:bg-red-900/20 p-4 rounded-lg border-l-4 border-red-500">
                <h4 className="font-semibold mb-2 text-red-700 dark:text-red-300">⚖️ Disciplinary Actions</h4>
                <ul className="space-y-2 text-sm">
                  <li>• Any ward found guilty of misconduct or breaking rules after warning will be asked to leave the hostel</li>
                  <li>• Indiscipline will not be tolerated - management has right to ask defaulters to leave</li>
                  <li>• Wards who produce forged signature of parents/LG will be expelled from hostel</li>
                  <li>• Perpetual offenders will be expelled</li>
                </ul>
              </div>
            </div>
          </EligibilitySection>

          {/* Meal Timings */}
          <EligibilitySection
            id="meals"
            title="Meal Timings & Daily Routine"
            icon={<Clock className="h-6 w-6" />}
            isDark={isDark}
            expanded={expandedSections.meals}
            onToggle={() => toggleSection('meals')}
            searchTerm={searchTerm}
          >
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <h4 className="font-semibold mb-3 text-orange-600">☀️ Summer Timings</h4>
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between p-2 bg-orange-50 dark:bg-orange-900/20 rounded">
                    <span><strong>Breakfast:</strong></span>
                    <span>0700h to 0800h</span>
                  </div>
                  <div className="flex justify-between p-2 bg-orange-50 dark:bg-orange-900/20 rounded">
                    <span><strong>Lunch:</strong></span>
                    <span>1230h to 1430h</span>
                  </div>
                  <div className="flex justify-between p-2 bg-orange-50 dark:bg-orange-900/20 rounded">
                    <span><strong>Dinner:</strong></span>
                    <span>2030h to 2130h</span>
                  </div>
                </div>
              </div>
              
              <div>
                <h4 className="font-semibold mb-3 text-blue-600">❄️ Winter Timings</h4>
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between p-2 bg-blue-50 dark:bg-blue-900/20 rounded">
                    <span><strong>Breakfast:</strong></span>
                    <span>0730h to 0830h</span>
                  </div>
                  <div className="flex justify-between p-2 bg-blue-50 dark:bg-blue-900/20 rounded">
                    <span><strong>Lunch:</strong></span>
                    <span>1300h to 1500h</span>
                  </div>
                  <div className="flex justify-between p-2 bg-blue-50 dark:bg-blue-900/20 rounded">
                    <span><strong>Dinner:</strong></span>
                    <span>2000h to 2100h</span>
                  </div>
                </div>
              </div>
              
              <div className="md:col-span-2">
                <div className="bg-green-50 dark:bg-green-900/20 p-4 rounded-lg border-l-4 border-green-500">
                  <h4 className="font-semibold mb-2 text-green-700 dark:text-green-300">📋 Meal Policies</h4>
                  <ul className="space-y-2 text-sm">
                    <li>• Meal timings will be strictly adhered to by all</li>
                    <li>• Catering staff will not be forced to provide meals before or after scheduled timings</li>
                    <li>• Packed lunch facility is available on prior notice of previous evening</li>
                    <li>• Sick wards may be allowed to have meals in their rooms with JCO Warden permission</li>
                    <li>• Timings in Summer and Winter season will be as mentioned above</li>
                  </ul>
                </div>
              </div>
            </div>
          </EligibilitySection>

          {/* Visitor Rules */}
          <EligibilitySection
            id="visitors"
            title="Visitor Rules & Local Guardian"
            icon={<Users className="h-6 w-6" />}
            isDark={isDark}
            expanded={expandedSections.visitors}
            onToggle={() => toggleSection('visitors')}
            searchTerm={searchTerm}
          >
            <div className="space-y-6">
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="font-semibold mb-3 text-purple-600">👥 Visitor Timings</h4>
                  <div className="space-y-2 text-sm">
                    <div className="p-3 bg-purple-50 dark:bg-purple-900/20 rounded">
                      <strong>Sundays and Holidays:</strong>
                      <br />Morning: 1000h to 1300h
                      <br />Evening: 1700h to 1900h
                    </div>
                    <div className="p-3 bg-purple-50 dark:bg-purple-900/20 rounded">
                      <strong>Working Days:</strong>
                      <br />Evening: 1700h to 1900h
                    </div>
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold mb-3 text-green-600">📝 Local Guardian (LG)</h4>
                  <ul className="space-y-2 text-sm">
                    <li>• Each ward should preferably have a local guardian (LG)</li>
                    <li>• LG will be introduced to OIC/Warden by parents at time of admission</li>
                    <li>• Guardian details on format mentioned in prospectus</li>
                    <li>• Change in LG and address must be intimated earliest on occurrence</li>
                  </ul>
                </div>
              </div>
              
              <div className="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-lg border-l-4 border-yellow-500">
                <h4 className="font-semibold mb-2 text-yellow-700 dark:text-yellow-300">⚠️ Visitor Restrictions</h4>
                <ul className="space-y-2 text-sm">
                  <li>• Specimen signatures of all approved visitors required (max 5 persons allowed)</li>
                  <li>• Hostel rooms are out of bounds for all visitors including close relatives</li>
                  <li>• Visitors may visit wards only in reception/visitors lounge</li>
                  <li>• Female visitors other than relatives not permitted to enter hostel building</li>
                  <li>• No tea/meals will be served to visitors - dining hall is OUT OF BOUNDS</li>
                  <li>• Wards not allowed to leave hostel complex with visitors</li>
                  <li>• Visitors not permitted to stay in hostel at night</li>
                  <li>• Hostel complex out of bounds for all old wards - meetings at main gate</li>
                </ul>
              </div>
            </div>
          </EligibilitySection>
        </div>
      </motion.div>
    </div>
  );
};

// Reusable Section Component
const EligibilitySection = ({ 
  id, 
  title, 
  icon, 
  children, 
  isDark, 
  expanded, 
  onToggle, 
  searchTerm 
}) => {
  const shouldShow = !searchTerm || title.toLowerCase().includes(searchTerm.toLowerCase());
  
  if (!shouldShow) return null;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <Card
        className={
          isDark
            ? "bg-black/30 border-white/10 backdrop-blur-md hover:bg-black/40 transition-all duration-300"
            : "bg-white/80 border-black/5 shadow-lg backdrop-blur-md hover:shadow-xl transition-all duration-300"
        }
      >
        <CardHeader
          className="cursor-pointer"
          onClick={onToggle}
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div
                className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                  isDark
                    ? "bg-gradient-to-br from-red-500/30 to-red-500/10"
                    : "bg-gradient-to-br from-red-500/20 to-red-500/5"
                }`}
              >
                {icon}
              </div>
              <CardTitle
                className={`text-xl font-semibold ${
                  isDark ? "text-white" : "text-gray-800"
                }`}
              >
                {title}
              </CardTitle>
            </div>
            {expanded ? (
              <ChevronUp className="h-5 w-5 text-gray-500" />
            ) : (
              <ChevronDown className="h-5 w-5 text-gray-500" />
            )}
          </div>
        </CardHeader>
        <AnimatePresence>
          {expanded && (
            <motion.div
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: "auto", opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 0.3 }}
            >
              <CardContent className="pt-0">
                {children}
              </CardContent>
            </motion.div>
          )}
        </AnimatePresence>
      </Card>
    </motion.div>
  );
};

export default EligibilityContainer;