"use client";

import { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Search, Filter, Users, 
  ArrowRight
} from 'lucide-react';
import Link from 'next/link';

export default function MentorsPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [showFilters, setShowFilters] = useState(false);

  // Mock data - no API calls
  const mentors = [];
  const isLoading = false;

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Header */}
      <div className="bg-white dark:bg-gray-800 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
                Find Your Mentor
              </h1>
              <p className="text-gray-600 dark:text-gray-400 mt-2">
                Connect with experienced VIPS-TC alumni who can guide your career journey
              </p>
            </div>
            <div className="mt-4 md:mt-0">
              <div className="text-sm text-gray-500 dark:text-gray-400">
                {mentors.length} mentors available
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Search and Filters */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-6 mb-8">
          <div className="flex flex-col md:flex-row gap-4">
            {/* Search */}
            <div className="flex-1 relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={20} />
              <input
                type="text"
                placeholder="Search by name, company, skills..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-vips-maroon-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
              />
            </div>

            {/* Filter Toggle */}
            <button
              onClick={() => setShowFilters(!showFilters)}
              className="flex items-center gap-2 px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
            >
              <Filter size={20} />
              Filters
            </button>
          </div>
        </div>

        {/* No Mentors State */}
        <div className="text-center py-12">
          <Users className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
            No mentors found
          </h3>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            No mentors are currently available. Check back later!
          </p>
          <Link href="/portal/mentorship">
            <button className="px-6 py-3 bg-vips-maroon-500 text-white rounded-lg hover:bg-vips-maroon-600 transition-colors flex items-center gap-2 mx-auto">
              <ArrowRight className="w-4 h-4" />
              Back to Mentorship Hub
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
}
