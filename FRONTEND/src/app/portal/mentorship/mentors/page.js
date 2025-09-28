"use client";

import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { 
  Search, Filter, Building2, Star, Users, 
  Clock, MessageCircle, AlertCircle, Loader2, ArrowRight
} from 'lucide-react';
import Link from 'next/link';
import { useGetMentors, useCreateMentorshipRequest } from '../../../../hooks/tanstack/useMentorship';
import { useSession } from 'next-auth/react';
import { enqueueSnackbar } from 'notistack';

export default function MentorsPage() {
  const { data: session } = useSession();
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredMentors, setFilteredMentors] = useState([]);

  // Re-enabled API hooks
  const { data: mentorsResponse, isLoading, error } = useGetMentors();
  const createMentorshipRequest = useCreateMentorshipRequest();
  const mentors = mentorsResponse || [];
  // Debug logging
  console.log('🔍 Debug Info:');
  console.log('- mentorsResponse:', mentorsResponse); 
  console.log('- mentors:', mentors);
  console.log('- isLoading:', isLoading);
  console.log('- error:', error);
  console.log('- session:', session);

  useEffect(() => {
    setFilteredMentors(mentors);
  }, [mentorsResponse]); // Use mentorsResponse instead of mentors

  const handleRequestMentorship = async (mentorId) => {
    if (!session?.user) {
      enqueueSnackbar('Please log in to request mentorship', { variant: 'error' });
      return;
    }
    try {
      await createMentorshipRequest.mutateAsync({
        mentor_id: mentorId,
        goals: "I would like to learn from your expertise.",
        duration_months: 3,
        preferred_communication: "video_call"
      });
      enqueueSnackbar('Mentorship request sent!', { variant: 'success' });
    } catch (error) {
      enqueueSnackbar('Failed to send request', { variant: 'error' });
    }
  };

  if (error) {
    return <div className="p-8 text-center">Error loading mentors: {error.message}</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="bg-white dark:bg-gray-800 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-8">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Find Your Mentor</h1>
          <p className="text-gray-600 dark:text-gray-400 mt-2">
            Connect with experienced VIPS-TC alumni
          </p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-8">
        {isLoading ? (
          <div className="text-center py-12">Loading mentors...</div>
        ) : filteredMentors.length > 0 ? (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredMentors.map((mentor) => (
              <div key={mentor.id} className="bg-white dark:bg-gray-800 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 p-6 hover:shadow-xl transition-shadow">
                <div className="flex items-center space-x-4 mb-4">
                  <div className="w-16 h-16 bg-vips-maroon-500 rounded-full flex items-center justify-center text-white font-bold text-xl">
                    {mentor.user?.first_name?.[0]}{mentor.user?.last_name?.[0]}
                  </div>
                  <div>
                    <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
                      {mentor.user?.first_name} {mentor.user?.last_name}
                    </h3>
                    <p className="text-gray-600">{mentor.current_position}</p>
                    <p className="text-sm text-gray-500">{mentor.current_company}</p>
                  </div>
                </div>
                
                <p className="text-gray-600 mb-4">{mentor.bio}</p>
                
                <div className="flex flex-wrap gap-2 mb-4">
                  {(mentor.expertise_areas || []).slice(0, 3).map((skill, index) => (
                    <span key={index} className="px-3 py-1 bg-vips-maroon-100 text-vips-maroon-700 rounded-full text-sm">
                      {skill}
                    </span>
                  ))}
                </div>

                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-500">{mentor.years_experience} years exp.</span>
                  <button 
                    onClick={() => handleRequestMentorship(mentor.id)}
                    className="px-4 py-2 bg-gray-300 text-black rounded-xl hover:bg-vips-maroon-600"
                  >
                    Request Mentorship
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-12">
            <h3 className="text-xl font-semibold mb-2">No mentors found</h3>
            <p className="text-gray-600">Check back later for available mentors!</p>
          </div>
        )}
      </div>
    </div>
  );
}
