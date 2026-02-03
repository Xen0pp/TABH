"use client";

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Building2, 
  Bed, 
  Users, 
  Utensils, 
  Dumbbell, 
  BookOpen, 
  Gamepad2, 
  Shirt,
  Camera,
  ChevronDown,
  ChevronUp,
  Star,
  Shield,
  Clock
} from 'lucide-react';

const RoomsFacilitiesContainer = () => {
  const [expandedSections, setExpandedSections] = useState({
    rooms: true,
    facilities: true
  });

  const toggleSection = (sectionId) => {
    setExpandedSections(prev => ({
      ...prev,
      [sectionId]: !prev[sectionId]
    }));
  };

  const roomTypes = [
    {
      id: 'double',
      title: 'Double Occupancy Room',
      capacity: '2 Students',
      description: 'Comfortable rooms designed for two students with attached bathroom and modern amenities.',
      features: [
        'Two single beds with quality mattresses',
        'Attached bathroom with geyser for winter bathing',
        'Study table and chair for each student',
        'Individual storage cupboards',
        'Desert cooler for comfort',
        'Balcony access (selected rooms)',
        '24/7 electricity backup'
      ],
      pricing: 'Standard hostel charges apply',
      popular: true
    },
    {
      id: 'dormitory',
      title: 'Dormitory (3-4 Students)',
      capacity: '3-4 Students',
      description: 'Economical accommodation option with shared facilities, perfect for building brotherhood.',
      features: [
        'Three to four single beds',
        'Common bathroom facilities',
        'Shared study area',
        'Individual storage lockers',
        'Common room access',
        'Rs 1000/- less than double room',
        'Great for making lifelong friendships'
      ],
      pricing: 'Reduced charges (Rs 1000/- less)',
      economical: true
    }
  ];

  const facilities = [
    {
      id: 'mess',
      title: 'Mess Facility',
      icon: <Utensils className="h-8 w-8" />,
      description: 'Hygienic and nutritious meals served in a clean, air-conditioned dining environment.',
      features: [
        'AC Dining Hall with modern ambiance',
        'Hygienic food by professional contractors',
        'Nutritious meals - Breakfast, Lunch & Dinner',
        '58" Colour LCD with TATA SKY in dining room',
        'Packed lunch facility on prior notice',
        'Special meals for sick students with JCO Warden permission',
        'Seasonal menu variations (Summer/Winter timings)'
      ],
      timings: {
        summer: {
          breakfast: '0700h to 0800h',
          lunch: '1230h to 1430h',
          dinner: '2030h to 2130h'
        },
        winter: {
          breakfast: '0730h to 0830h',
          lunch: '1300h to 1500h',
          dinner: '2000h to 2100h'
        }
      },
      color: 'green'
    },
    {
      id: 'gym',
      title: 'Fitness Center/Gym',
      icon: <Dumbbell className="h-8 w-8" />,
      description: 'Well-equipped multi-station gym for maintaining physical fitness and health.',
      features: [
        'Multi-station gym equipment for health benefits',
        'Cardio and strength training machines',
        'Free weights and dumbbells',
        'Professional fitness equipment',
        'Spacious workout area',
        'Health and fitness guidance available',
        'Regular equipment maintenance'
      ],
      timings: 'Available throughout the day',
      color: 'red'
    },
    {
      id: 'study',
      title: 'Study Hall & Library',
      icon: <BookOpen className="h-8 w-8" />,
      description: 'Quiet and conducive environment for academic pursuits and learning.',
      features: [
        'Library with sufficient number of books',
        'Quiet study halls for focused learning',
        'Daily newspapers and magazines in common room',
        'Reference books and study materials',
        'Individual study spaces with table and chair',
        'Group study areas available',
        'Extended hours during examination periods'
      ],
      timings: 'Extended hours available',
      color: 'blue'
    },
    {
      id: 'recreation',
      title: 'Recreation Activity Space',
      icon: <Gamepad2 className="h-8 w-8" />,
      description: 'Entertainment and recreational facilities for relaxation and social interaction.',
      features: [
        'Badminton court for sports activities',
        'Chess and indoor games facility',
        'Recreation room with cable TV',
        'Two beautiful lawns/gardens for relaxation',
        'Common areas for socializing',
        'Entertainment systems',
        'Outdoor relaxation spaces'
      ],
      timings: 'Available during leisure hours',
      color: 'purple'
    },
    {
      id: 'laundry',
      title: 'Laundry Services',
      icon: <Shirt className="h-8 w-8" />,
      description: 'Professional laundry services to keep your clothes clean and fresh.',
      features: [
        'Free laundry services for all residents',
        'Modern laundry service equipment',
        'Professional cleaning standards',
        'Regular pickup and delivery schedule',
        'Stain removal services available',
        'Quick turnaround time',
        'Hygienic washing processes'
      ],
      timings: 'Daily service available',
      color: 'cyan'
    }
  ];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        duration: 0.6,
        staggerChildren: 0.1
      }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.5 }
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
      <motion.div
        className="container mx-auto px-4 py-8"
        variants={containerVariants}
        initial="hidden"
        animate="visible"
      >
        {/* Header */}
        <motion.div className="text-center mb-12" variants={itemVariants}>
          <div className="flex items-center justify-center gap-3 mb-4">
            <Building2 className="h-12 w-12 text-red-600" />
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white">
              Rooms & Facilities
            </h1>
          </div>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
            Discover comfortable accommodation and world-class facilities at Tauras Army Boys Hostel
          </p>
        </motion.div>

        {/* Quick Stats */}
        <motion.div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12" variants={itemVariants}>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg text-center">
            <Bed className="h-8 w-8 text-red-600 mx-auto mb-2" />
            <div className="text-2xl font-bold text-gray-900 dark:text-white">2 Types</div>
            <div className="text-sm text-gray-600 dark:text-gray-300">Room Options</div>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg text-center">
            <Users className="h-8 w-8 text-green-600 mx-auto mb-2" />
            <div className="text-2xl font-bold text-gray-900 dark:text-white">2-4</div>
            <div className="text-sm text-gray-600 dark:text-gray-300">Students/Room</div>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg text-center">
            <Star className="h-8 w-8 text-yellow-600 mx-auto mb-2" />
            <div className="text-2xl font-bold text-gray-900 dark:text-white">5</div>
            <div className="text-sm text-gray-600 dark:text-gray-300">Key Facilities</div>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg text-center">
            <Shield className="h-8 w-8 text-blue-600 mx-auto mb-2" />
            <div className="text-2xl font-bold text-gray-900 dark:text-white">24/7</div>
            <div className="text-sm text-gray-600 dark:text-gray-300">Security</div>
          </div>
        </motion.div>

        {/* Rooms Section */}
        <motion.div className="mb-12" variants={itemVariants}>
          <div 
            className="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden cursor-pointer"
            onClick={() => toggleSection('rooms')}
          >
            <div className="p-6 border-b border-gray-200 dark:border-gray-700">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <Bed className="h-6 w-6 text-red-600" />
                  <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                    Accommodation Options
                  </h2>
                </div>
                {expandedSections.rooms ? (
                  <ChevronUp className="h-6 w-6 text-gray-500" />
                ) : (
                  <ChevronDown className="h-6 w-6 text-gray-500" />
                )}
              </div>
            </div>
            
            {expandedSections.rooms && (
              <div className="p-6">
                <div className="grid md:grid-cols-2 gap-8">
                  {roomTypes.map((room) => (
                    <motion.div
                      key={room.id}
                      className="bg-gray-50 dark:bg-gray-700 rounded-lg p-6 relative"
                      whileHover={{ scale: 1.02 }}
                      transition={{ duration: 0.2 }}
                    >
                      {room.popular && (
                        <div className="absolute -top-2 -right-2 bg-red-600 text-white px-3 py-1 rounded-full text-sm font-semibold">
                          Most Popular
                        </div>
                      )}
                      {room.economical && (
                        <div className="absolute -top-2 -right-2 bg-green-600 text-white px-3 py-1 rounded-full text-sm font-semibold">
                          Economical
                        </div>
                      )}
                      
                      <div className="flex items-center gap-3 mb-4">
                        <Building2 className="h-8 w-8 text-red-600" />
                        <div>
                          <h3 className="text-xl font-bold text-gray-900 dark:text-white">
                            {room.title}
                          </h3>
                          <p className="text-red-600 font-semibold">{room.capacity}</p>
                        </div>
                      </div>
                      
                      <p className="text-gray-600 dark:text-gray-300 mb-4">
                        {room.description}
                      </p>
                      
                      <div className="mb-4">
                        <h4 className="font-semibold text-gray-900 dark:text-white mb-2">Features:</h4>
                        <ul className="space-y-1">
                          {room.features.map((feature, index) => (
                            <li key={index} className="text-sm text-gray-600 dark:text-gray-300 flex items-start gap-2">
                              <span className="text-red-600 mt-1">•</span>
                              {feature}
                            </li>
                          ))}
                        </ul>
                      </div>
                      
                      <div className="bg-white dark:bg-gray-600 p-3 rounded-lg mb-4">
                        <div className="flex items-center justify-between">
                          <span className="font-semibold text-gray-900 dark:text-white">Pricing:</span>
                          <span className="text-red-600 font-semibold">{room.pricing}</span>
                        </div>
                      </div>
                      
                      {/* Placeholder for room image */}
                      <div className="bg-gray-200 dark:bg-gray-600 rounded-lg h-48 flex items-center justify-center">
                        <div className="text-center text-gray-500 dark:text-gray-400">
                          <Camera className="h-12 w-12 mx-auto mb-2" />
                          <p>Room Image</p>
                          <p className="text-sm">(Upload via Admin Panel)</p>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </motion.div>

        {/* Facilities Section */}
        <motion.div variants={itemVariants}>
          <div 
            className="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden cursor-pointer"
            onClick={() => toggleSection('facilities')}
          >
            <div className="p-6 border-b border-gray-200 dark:border-gray-700">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <Star className="h-6 w-6 text-red-600" />
                  <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                    World-Class Facilities
                  </h2>
                </div>
                {expandedSections.facilities ? (
                  <ChevronUp className="h-6 w-6 text-gray-500" />
                ) : (
                  <ChevronDown className="h-6 w-6 text-gray-500" />
                )}
              </div>
            </div>
            
            {expandedSections.facilities && (
              <div className="p-6">
                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {facilities.map((facility) => (
                    <motion.div
                      key={facility.id}
                      className="bg-gray-50 dark:bg-gray-700 rounded-lg p-6"
                      whileHover={{ scale: 1.02 }}
                      transition={{ duration: 0.2 }}
                    >
                      <div className={`flex items-center gap-3 mb-4 text-${facility.color}-600`}>
                        {facility.icon}
                        <h3 className="text-xl font-bold text-gray-900 dark:text-white">
                          {facility.title}
                        </h3>
                      </div>
                      
                      <p className="text-gray-600 dark:text-gray-300 mb-4">
                        {facility.description}
                      </p>
                      
                      <div className="mb-4">
                        <h4 className="font-semibold text-gray-900 dark:text-white mb-2">Features:</h4>
                        <ul className="space-y-1">
                          {facility.features.map((feature, index) => (
                            <li key={index} className="text-sm text-gray-600 dark:text-gray-300 flex items-start gap-2">
                              <span className={`text-${facility.color}-600 mt-1`}>•</span>
                              {feature}
                            </li>
                          ))}
                        </ul>
                      </div>
                      
                      {facility.timings && (
                        <div className="bg-white dark:bg-gray-600 p-3 rounded-lg mb-4">
                          <div className="flex items-center gap-2 mb-2">
                            <Clock className="h-4 w-4 text-gray-600 dark:text-gray-300" />
                            <span className="font-semibold text-gray-900 dark:text-white">Timings:</span>
                          </div>
                          {typeof facility.timings === 'string' ? (
                            <p className="text-sm text-gray-600 dark:text-gray-300">{facility.timings}</p>
                          ) : (
                            <div className="space-y-2">
                              <div>
                                <p className="text-sm font-semibold text-orange-600">☀️ Summer:</p>
                                <p className="text-xs text-gray-600 dark:text-gray-300">
                                  Breakfast: {facility.timings.summer.breakfast} | 
                                  Lunch: {facility.timings.summer.lunch} | 
                                  Dinner: {facility.timings.summer.dinner}
                                </p>
                              </div>
                              <div>
                                <p className="text-sm font-semibold text-blue-600">❄️ Winter:</p>
                                <p className="text-xs text-gray-600 dark:text-gray-300">
                                  Breakfast: {facility.timings.winter.breakfast} | 
                                  Lunch: {facility.timings.winter.lunch} | 
                                  Dinner: {facility.timings.winter.dinner}
                                </p>
                              </div>
                            </div>
                          )}
                        </div>
                      )}
                      
                      {/* Placeholder for facility image */}
                      <div className="bg-gray-200 dark:bg-gray-600 rounded-lg h-40 flex items-center justify-center">
                        <div className="text-center text-gray-500 dark:text-gray-400">
                          <Camera className="h-8 w-8 mx-auto mb-2" />
                          <p className="text-sm">Facility Image</p>
                          <p className="text-xs">(Upload via Admin Panel)</p>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </motion.div>

        {/* Additional Information */}
        <motion.div className="mt-12 bg-red-50 dark:bg-red-900/20 p-6 rounded-lg border-l-4 border-red-500" variants={itemVariants}>
          <h3 className="font-semibold text-red-700 dark:text-red-300 mb-2">📋 Important Notes</h3>
          <ul className="space-y-2 text-sm text-red-600 dark:text-red-400">
            <li>• All facilities are available 24/7 with round-the-clock security arrangements</li>
            <li>• Room allocation is based on priority system and availability</li>
            <li>• Facility usage guidelines must be followed by all residents</li>
            <li>• Images can be uploaded and managed through the admin panel</li>
            <li>• For specific facility timings and bookings, contact hostel administration</li>
            <li>• RO Water purification system with water cooler available in every building</li>
          </ul>
        </motion.div>
      </motion.div>
    </div>
  );
};

export default RoomsFacilitiesContainer;