"use client";

import { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Users, ArrowRight
} from 'lucide-react';
import Link from 'next/link';

export default function MyMentorshipsPage() {
  const [activeTab, setActiveTab] = useState('all');
  
  // Mock data - no API calls
  const mentorships = [];
  const isLoading = false;

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Header */}
      <div className="bg-white dark:bg-gray-800 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
                My Mentorships
              </h1>
              <p className="text-gray-600 dark:text-gray-400 mt-2">
                Track your mentorship requests and active mentoring relationships
              </p>
            </div>
            <div className="mt-4 md:mt-0">
              <Link href="/portal/mentorship/mentors">
                <button className="px-4 py-2 bg-vips-maroon-500 text-white rounded-lg hover:bg-vips-maroon-600 transition-colors flex items-center gap-2">
                  <Users className="w-4 h-4" />
                  Find More Mentors
                </button>
              </Link>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Tabs */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-6 mb-8">
          <div className="flex space-x-1 bg-gray-100 dark:bg-gray-700 rounded-lg p-1">
            {[
              { key: 'all', label: 'All Requests' },
              { key: 'pending', label: 'Pending' },
              { key: 'accepted', label: 'Active' },
              { key: 'completed', label: 'Completed' }
            ].map((tab) => (
              <button
                key={tab.key}
                onClick={() => setActiveTab(tab.key)}
                className={`flex-1 py-2 px-4 text-sm font-medium rounded-md transition-colors ${
                  activeTab === tab.key
                    ? 'bg-white dark:bg-gray-800 text-vips-maroon-600 shadow-sm'
                    : 'text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </div>

        {/* Empty State */}
        <div className="text-center py-12">
          <Users className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
            No mentorships found
          </h3>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            You haven't requested any mentorships yet. Start by finding a mentor!
          </p>
          <Link href="/portal/mentorship/mentors">
            <button className="px-6 py-3 bg-vips-maroon-500 text-white rounded-lg hover:bg-vips-maroon-600 transition-colors flex items-center gap-2 mx-auto">
              <Users className="w-5 h-5" />
              Find Mentors
              <ArrowRight className="w-4 h-4" />
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
}
