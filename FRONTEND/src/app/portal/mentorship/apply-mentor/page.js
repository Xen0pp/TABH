"use client";

import { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  User, Briefcase, Award, Clock, Users, Link as LinkIcon, 
  Plus, X, CheckCircle, AlertCircle, ArrowLeft 
} from 'lucide-react';
import Link from 'next/link';

export default function ApplyMentorPage() {
  const [formData, setFormData] = useState({
    expertise_areas: [],
    years_experience: '',
    current_company: '',
    current_position: '',
    mentoring_capacity: 3,
    bio: '',
    linkedin_url: '',
    github_url: '',
    portfolio_url: '',
    availability: {
      weekdays: [],
      weekends: false,
      preferred_time: ''
    }
  });

  const [newExpertise, setNewExpertise] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [errors, setErrors] = useState({});

  const expertiseOptions = [
    'Web Development', 'Mobile Development', 'Data Science', 'Machine Learning',
    'DevOps', 'Cloud Computing', 'Cybersecurity', 'UI/UX Design',
    'Product Management', 'Digital Marketing', 'Business Development',
    'Entrepreneurship', 'Finance', 'Consulting'
  ];

  const weekdayOptions = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
  ];

  const timeOptions = [
    'Morning (9 AM - 12 PM)', 'Afternoon (12 PM - 5 PM)', 
    'Evening (5 PM - 8 PM)', 'Flexible'
  ];

  const handleInputChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }));
    // Clear error when user starts typing
    if (errors[field]) {
      setErrors(prev => ({
        ...prev,
        [field]: ''
      }));
    }
  };

  const handleAvailabilityChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      availability: {
        ...prev.availability,
        [field]: value
      }
    }));
  };

  const addExpertise = (expertise) => {
    if (expertise && !formData.expertise_areas.includes(expertise)) {
      setFormData(prev => ({
        ...prev,
        expertise_areas: [...prev.expertise_areas, expertise]
      }));
      setNewExpertise('');
    }
  };

  const removeExpertise = (expertise) => {
    setFormData(prev => ({
      ...prev,
      expertise_areas: prev.expertise_areas.filter(item => item !== expertise)
    }));
  };

  const validateForm = () => {
    const newErrors = {};

    if (!formData.current_company.trim()) {
      newErrors.current_company = 'Current company is required';
    }
    if (!formData.current_position.trim()) {
      newErrors.current_position = 'Current position is required';
    }
    if (!formData.years_experience || formData.years_experience < 1) {
      newErrors.years_experience = 'Please enter valid years of experience';
    }
    if (formData.expertise_areas.length === 0) {
      newErrors.expertise_areas = 'Please add at least one expertise area';
    }
    if (!formData.bio.trim() || formData.bio.length < 50) {
      newErrors.bio = 'Bio must be at least 50 characters long';
    }
    if (formData.linkedin_url && !formData.linkedin_url.includes('linkedin.com')) {
      newErrors.linkedin_url = 'Please enter a valid LinkedIn URL';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setIsSubmitting(true);

    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      setSubmitted(true);
    } catch (error) {
      console.error('Error submitting application:', error);
    } finally {
      setIsSubmitting(false);
    }
  };

  if (submitted) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center">
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8 max-w-md w-full mx-4"
        >
          <div className="text-center">
            <CheckCircle className="w-16 h-16 text-green-500 mx-auto mb-4" />
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
              Application Submitted!
            </h2>
            <p className="text-gray-600 dark:text-gray-400 mb-6">
              Thank you for applying to become a mentor. Our team will review your application and get back to you within 2-3 business days.
            </p>
            <Link href="/portal/mentorship">
              <button className="w-full bg-vips-maroon-500 text-white py-3 rounded-lg hover:bg-vips-maroon-600 transition-colors">
                Back to Mentorship Hub
              </button>
            </Link>
          </div>
        </motion.div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* Header */}
      <div className="bg-white dark:bg-gray-800 shadow-sm">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="flex items-center gap-4">
            <Link href="/portal/mentorship">
              <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors">
                <ArrowLeft size={20} />
              </button>
            </Link>
            <div>
              <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
                Become a Mentor
              </h1>
              <p className="text-gray-600 dark:text-gray-400 mt-2">
                Share your expertise and help VIPS-TC students achieve their goals
              </p>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <form onSubmit={handleSubmit} className="space-y-8">
          {/* Professional Information */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6"
          >
            <div className="flex items-center gap-3 mb-6">
              <Briefcase className="w-6 h-6 text-vips-maroon-500" />
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white">
                Professional Information
              </h2>
            </div>

            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Current Company *
                </label>
                <input
                  type="text"
                  value={formData.current_company}
                  onChange={(e) => handleInputChange('current_company', e.target.value)}
                  className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-vips-maroon-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                    errors.current_company ? 'border-red-500' : 'border-gray-300 dark:border-gray-600'
                  }`}
                  placeholder="e.g., Google, Microsoft, Startup Inc."
                />
                {errors.current_company && (
                  <p className="text-red-500 text-sm mt-1">{errors.current_company}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Current Position *
                </label>
                <input
                  type="text"
                  value={formData.current_position}
                  onChange={(e) => handleInputChange('current_position', e.target.value)}
                  className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-vips-maroon-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                    errors.current_position ? 'border-red-500' : 'border-gray-300 dark:border-gray-600'
                  }`}
                  placeholder="e.g., Senior Software Engineer, Product Manager"
                />
                {errors.current_position && (
                  <p className="text-red-500 text-sm mt-1">{errors.current_position}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Years of Experience *
                </label>
                <input
                  type="number"
                  min="1"
                  max="50"
                  value={formData.years_experience}
                  onChange={(e) => handleInputChange('years_experience', parseInt(e.target.value))}
                  className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-vips-maroon-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                    errors.years_experience ? 'border-red-500' : 'border-gray-300 dark:border-gray-600'
                  }`}
                  placeholder="5"
                />
                {errors.years_experience && (
                  <p className="text-red-500 text-sm mt-1">{errors.years_experience}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Mentoring Capacity
                </label>
                <select
                  value={formData.mentoring_capacity}
                  onChange={(e) => handleInputChange('mentoring_capacity', parseInt(e.target.value))}
                  className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-vips-maroon-500 dark:bg-gray-700 dark:text-white"
                >
                  <option value={1}>1 mentee at a time</option>
                  <option value={2}>2 mentees at a time</option>
                  <option value={3}>3 mentees at a time</option>
                  <option value={4}>4 mentees at a time</option>
                  <option value={5}>5 mentees at a time</option>
                </select>
              </div>
            </div>
          </motion.div>

          {/* Expertise Areas */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6"
          >
            <div className="flex items-center gap-3 mb-6">
              <Award className="w-6 h-6 text-vips-maroon-500" />
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white">
                Expertise Areas
              </h2>
            </div>

            <div className="mb-4">
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Add your areas of expertise *
              </label>
              <div className="flex gap-2">
                <select
                  value={newExpertise}
                  onChange={(e) => setNewExpertise(e.target.value)}
                  className="flex-1 px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-vips-maroon-500 dark:bg-gray-700 dark:text-white"
                >
                  <option value="">Select an expertise area</option>
                  {expertiseOptions.map(option => (
                    <option key={option} value={option}>{option}</option>
                  ))}
                </select>
                <button
                  type="button"
                  onClick={() => addExpertise(newExpertise)}
                  className="px-4 py-3 bg-vips-maroon-500 text-white rounded-lg hover:bg-vips-maroon-600 transition-colors"
                >
                  <Plus size={20} />
                </button>
              </div>
              {errors.expertise_areas && (
                <p className="text-red-500 text-sm mt-1">{errors.expertise_areas}</p>
              )}
            </div>

            {formData.expertise_areas.length > 0 && (
              <div className="flex flex-wrap gap-2">
                {formData.expertise_areas.map((expertise, index) => (
                  <span
                    key={index}
                    className="flex items-center gap-2 px-3 py-1 bg-vips-maroon-100 text-vips-maroon-700 dark:bg-vips-maroon-900 dark:text-vips-maroon-300 rounded-full text-sm"
                  >
                    {expertise}
                    <button
                      type="button"
                      onClick={() => removeExpertise(expertise)}
                      className="hover:bg-vips-maroon-200 dark:hover:bg-vips-maroon-800 rounded-full p-1"
                    >
                      <X size={14} />
                    </button>
                  </span>
                ))}
              </div>
            )}
          </motion.div>

          {/* Bio */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6"
          >
            <div className="flex items-center gap-3 mb-6">
              <User className="w-6 h-6 text-vips-maroon-500" />
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white">
                About You
              </h2>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Bio & Mentoring Philosophy *
              </label>
              <textarea
                rows={6}
                value={formData.bio}
                onChange={(e) => handleInputChange('bio', e.target.value)}
                className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-vips-maroon-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                  errors.bio ? 'border-red-500' : 'border-gray-300 dark:border-gray-600'
                }`}
                placeholder="Tell us about your background, experience, and what motivates you to mentor students. What can you help them with? (minimum 50 characters)"
              />
              <div className="flex justify-between items-center mt-1">
                {errors.bio && (
                  <p className="text-red-500 text-sm">{errors.bio}</p>
                )}
                <p className="text-sm text-gray-500 dark:text-gray-400 ml-auto">
                  {formData.bio.length}/50 minimum
                </p>
              </div>
            </div>
          </motion.div>

          {/* Social Links */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6"
          >
            <div className="flex items-center gap-3 mb-6">
              <LinkIcon className="w-6 h-6 text-vips-maroon-500" />
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white">
                Professional Links
              </h2>
            </div>

            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  LinkedIn Profile
                </label>
                <input
                  type="url"
                  value={formData.linkedin_url}
                  onChange={(e) => handleInputChange('linkedin_url', e.target.value)}
                  className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-vips-maroon-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                    errors.linkedin_url ? 'border-red-500' : 'border-gray-300 dark:border-gray-600'
                  }`}
                  placeholder="https://linkedin.com/in/yourprofile"
                />
                {errors.linkedin_url && (
                  <p className="text-red-500 text-sm mt-1">{errors.linkedin_url}</p>
                )}
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  GitHub Profile (Optional)
                </label>
                <input
                  type="url"
                  value={formData.github_url}
                  onChange={(e) => handleInputChange('github_url', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-vips-maroon-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
                  placeholder="https://github.com/yourusername"
                />
              </div>

              <div className="md:col-span-2">
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  Portfolio/Website (Optional)
                </label>
                <input
                  type="url"
                  value={formData.portfolio_url}
                  onChange={(e) => handleInputChange('portfolio_url', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-vips-maroon-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
                  placeholder="https://yourportfolio.com"
                />
              </div>
            </div>
          </motion.div>

          {/* Submit Button */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="flex justify-end"
          >
            <button
              type="submit"
              disabled={isSubmitting}
              className="px-8 py-3 bg-vips-maroon-500 text-white rounded-lg hover:bg-vips-maroon-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
            >
              {isSubmitting ? (
                <>
                  <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                  Submitting...
                </>
              ) : (
                'Submit Application'
              )}
            </button>
          </motion.div>
        </form>
      </div>
    </div>
  );
}
