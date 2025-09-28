"use client";

import { useState } from 'react';
import { motion } from 'framer-motion';
import { Users, BookOpen, Target, ArrowRight } from 'lucide-react';
import Link from 'next/link';

export default function MentorshipHub() {
  const [stats] = useState({
    totalMentors: 12,
    activeMentorships: 5,
    completedSessions: 23,
    successRate: 95
  });

  const features = [
    {
      icon: Users,
      title: "Find Your Mentor",
      description: "Connect with experienced alumni who can guide your career journey",
      link: "/portal/mentorship/mentors",
      color: "from-blue-500 to-blue-600",
      stats: `${stats.totalMentors} mentors available`
    },
    {
      icon: Target,
      title: "My Mentorships",
      description: "Track your mentorship requests and active relationships",
      link: "/portal/mentorship/my-mentorships",
      color: "from-green-500 to-green-600",
      stats: `${stats.activeMentorships} active mentorships`
    },
    {
      icon: BookOpen,
      title: "Apply as Mentor",
      description: "Share your expertise and help guide the next generation",
      link: "/portal/mentorship/apply-mentor",
      color: "from-purple-500 to-purple-600",
      stats: "Help others grow"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-vips-maroon-600 to-vips-maroon-800 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center"
          >
            <h1 className="text-4xl md:text-6xl font-bold mb-6 text-black">
              Mentorship Hub
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-black">
              Connect, Learn, and Grow with VIPS-TC Alumni Network
            </p>
          </motion.div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Features Grid */}
        <div className="grid md:grid-cols-3 gap-6 mb-12">
          {features.map((feature, index) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
            >
              <Link href={feature.link}>
                <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 p-6 cursor-pointer group hover:-translate-y-2">
                  <div className={`w-12 h-12 bg-gradient-to-r ${feature.color} rounded-lg flex items-center justify-center mb-4 group-hover:scale-110 transition-transform`}>
                    <feature.icon className="w-6 h-6 text-white" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600 dark:text-gray-400 mb-4">
                    {feature.description}
                  </p>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-500">{feature.stats}</span>
                    <ArrowRight className="w-4 h-4 text-gray-400 group-hover:text-vips-maroon-500 group-hover:translate-x-1 transition-all" />
                  </div>
                </div>
              </Link>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}