"use client";

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Camera, 
  Search, 
  Filter, 
  Calendar, 
  Tag, 
  Users, 
  Star,
  Grid3X3,
  List,
  X,
  ChevronLeft,
  ChevronRight,
  Heart,
  MessageCircle,
  Share2,
  Download,
  Eye,
  MapPin,
  Clock
} from 'lucide-react';

const GalleryContainer = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [viewMode, setViewMode] = useState('grid'); // grid, list, timeline
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedTag, setSelectedTag] = useState('all');
  const [dateFilter, setDateFilter] = useState('all');
  const [showFilters, setShowFilters] = useState(false);
  const [images, setImages] = useState([]);
  const [categories, setCategories] = useState([]);
  const [featuredTags, setFeaturedTags] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // API calls
  const fetchGalleryData = async () => {
    try {
      setLoading(true);
      setError(null);
      
      // Build query parameters
      const params = new URLSearchParams();
      if (selectedCategory !== 'all') params.append('category', selectedCategory);
      if (selectedTag !== 'all') params.append('tag', selectedTag);
      if (searchTerm) params.append('search', searchTerm);
      
      // Fetch images, categories, and tags in parallel
      const baseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001/api/v1';
      const [imagesRes, categoriesRes, tagsRes] = await Promise.all([
        fetch(`${baseUrl}/gallery/images/?${params}`),
        fetch(`${baseUrl}/gallery/categories/`),
        fetch(`${baseUrl}/gallery/tags/`)
      ]);
      
      if (!imagesRes.ok || !categoriesRes.ok || !tagsRes.ok) {
        throw new Error('Failed to fetch gallery data');
      }
      
      const [imagesData, categoriesData, tagsData] = await Promise.all([
        imagesRes.json(),
        categoriesRes.json(),
        tagsRes.json()
      ]);
      
      setImages(imagesData.results || []);
      setCategories(categoriesData.results || []);
      setFeaturedTags(tagsData.results || []);
      
    } catch (err) {
      console.error('Error fetching gallery data:', err);
      console.error('Error details:', err.message);
      setError(`Failed to load gallery data: ${err.message}`);
      // Fallback to empty arrays
      setImages([]);
      setCategories([]);
      setFeaturedTags([]);
    } finally {
      setLoading(false);
    }
  };

  // Fetch data on component mount and when filters change
  useEffect(() => {
    fetchGalleryData();
  }, [selectedCategory, selectedTag, searchTerm]);

  const filteredImages = images;

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <motion.div 
          className="text-center mb-12"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <div className="flex items-center justify-center gap-3 mb-4">
            <Camera className="h-12 w-12 text-red-600" />
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white">
              TABH Gallery
            </h1>
          </div>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
            Capturing memories, celebrating moments, and preserving the spirit of brotherhood at Tauras Army Boys Hostel
          </p>
        </motion.div>

        {/* Search and Filters */}
        <motion.div 
          className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 mb-8"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
        >
          <div className="flex flex-col md:flex-row gap-4 items-center justify-between">
            {/* Search */}
            <div className="relative flex-1 max-w-md">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-5 w-5" />
              <input
                type="text"
                placeholder="Search photos, events, people..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              />
            </div>

            {/* View Mode Toggle */}
            <div className="flex items-center gap-2 bg-gray-100 dark:bg-gray-700 rounded-lg p-1">
              <button
                onClick={() => setViewMode('grid')}
                className={`p-2 rounded ${viewMode === 'grid' ? 'bg-red-600 text-white' : 'text-gray-600 dark:text-gray-300'}`}
              >
                <Grid3X3 className="h-4 w-4" />
              </button>
              <button
                onClick={() => setViewMode('list')}
                className={`p-2 rounded ${viewMode === 'list' ? 'bg-red-600 text-white' : 'text-gray-600 dark:text-gray-300'}`}
              >
                <List className="h-4 w-4" />
              </button>
            </div>

            {/* Filter Toggle */}
            <button
              onClick={() => setShowFilters(!showFilters)}
              className="flex items-center gap-2 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
            >
              <Filter className="h-4 w-4" />
              Filters
            </button>
          </div>

          {/* Filters Panel */}
          <AnimatePresence>
            {showFilters && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                exit={{ opacity: 0, height: 0 }}
                className="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700"
              >
                <div className="grid md:grid-cols-3 gap-6">
                  {/* Categories */}
                  <div>
                    <h3 className="font-semibold text-gray-900 dark:text-white mb-3 flex items-center gap-2">
                      <Tag className="h-4 w-4" />
                      Categories
                    </h3>
                    <div className="space-y-2">
                      {categories.map(category => (
                        <button
                          key={category.id}
                          onClick={() => setSelectedCategory(category.category_type || category.id)}
                          className={`w-full text-left px-3 py-2 rounded-lg transition-colors ${
                            selectedCategory === (category.category_type || category.id)
                              ? 'bg-red-100 dark:bg-red-900/20 text-red-700 dark:text-red-300'
                              : 'hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-300'
                          }`}
                        >
                          <div className="flex items-center justify-between">
                            <span className="text-sm">{category.name}</span>
                            <span className="text-xs bg-gray-200 dark:bg-gray-600 px-2 py-1 rounded">
                              {category.count}
                            </span>
                          </div>
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Featured Tags */}
                  <div>
                    <h3 className="font-semibold text-gray-900 dark:text-white mb-3 flex items-center gap-2">
                      <Star className="h-4 w-4" />
                      Popular Tags
                    </h3>
                    <div className="flex flex-wrap gap-2">
                      {featuredTags.map(tag => (
                        <button
                          key={tag}
                          onClick={() => setSelectedTag(selectedTag === tag ? 'all' : tag)}
                          className={`px-3 py-1 rounded-full text-sm transition-colors ${
                            selectedTag === tag
                              ? 'bg-red-600 text-white'
                              : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'
                          }`}
                        >
                          {tag}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Date Filter */}
                  <div>
                    <h3 className="font-semibold text-gray-900 dark:text-white mb-3 flex items-center gap-2">
                      <Calendar className="h-4 w-4" />
                      Date Range
                    </h3>
                    <select
                      value={dateFilter}
                      onChange={(e) => setDateFilter(e.target.value)}
                      className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                    >
                      <option value="all">All Time</option>
                      <option value="this_month">This Month</option>
                      <option value="last_month">Last Month</option>
                      <option value="this_year">This Year</option>
                      <option value="last_year">Last Year</option>
                    </select>
                  </div>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>

        {/* Results Summary */}
        <div className="flex items-center justify-between mb-6">
          <p className="text-gray-600 dark:text-gray-300">
            {loading ? 'Loading...' : `Showing ${filteredImages.length} photos`}
          </p>
          {(searchTerm || selectedCategory !== 'all' || selectedTag !== 'all') && (
            <button
              onClick={() => {
                setSearchTerm('');
                setSelectedCategory('all');
                setSelectedTag('all');
                setDateFilter('all');
              }}
              className="text-red-600 hover:text-red-700 text-sm font-medium"
            >
              Clear Filters
            </button>
          )}
        </div>

        {/* Loading State */}
        {loading && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-center py-16"
          >
            <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-red-600 mx-auto mb-4"></div>
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
              Loading Gallery...
            </h3>
            <p className="text-gray-600 dark:text-gray-300">
              Please wait while we fetch the latest photos
            </p>
          </motion.div>
        )}

        {/* Error State */}
        {error && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-center py-16"
          >
            <Camera className="h-16 w-16 text-red-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
              Error Loading Gallery
            </h3>
            <p className="text-gray-600 dark:text-gray-300 mb-4">
              {error}
            </p>
            <button
              onClick={fetchGalleryData}
              className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
            >
              Try Again
            </button>
          </motion.div>
        )}

        {/* Gallery Grid */}
        {!loading && !error && (
          <motion.div 
            className={`grid gap-6 ${
              viewMode === 'grid' 
                ? 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4' 
                : 'grid-cols-1'
            }`}
            layout
          >
          {filteredImages.map((image, index) => (
            <motion.div
              key={image.id}
              layout
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.3, delay: index * 0.1 }}
              className={`bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden cursor-pointer group ${
                viewMode === 'list' ? 'flex' : ''
              }`}
              onClick={() => setSelectedImage(image)}
              whileHover={{ scale: 1.02 }}
            >
              {/* Image */}
              <div className={`relative ${viewMode === 'list' ? 'w-48 h-32' : 'aspect-square'}`}>
                <div className="w-full h-full bg-gray-200 dark:bg-gray-700 flex items-center justify-center">
                  <Camera className="h-12 w-12 text-gray-400" />
                  <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-all duration-300" />
                </div>
                
                {/* Priority Badge */}
                {image.priority === 'featured' && (
                  <div className="absolute top-2 left-2 bg-red-600 text-white px-2 py-1 rounded-full text-xs font-semibold">
                    Featured
                  </div>
                )}
                
                {/* View Count */}
                <div className="absolute bottom-2 right-2 bg-black bg-opacity-50 text-white px-2 py-1 rounded text-xs flex items-center gap-1">
                  <Eye className="h-3 w-3" />
                  {image.view_count}
                </div>
              </div>

              {/* Content */}
              <div className={`p-4 ${viewMode === 'list' ? 'flex-1' : ''}`}>
                <h3 className="font-semibold text-gray-900 dark:text-white mb-2 line-clamp-2">
                  {image.title}
                </h3>
                
                <p className="text-sm text-gray-600 dark:text-gray-300 mb-3 line-clamp-2">
                  {image.description}
                </p>
                
                {/* Metadata */}
                <div className="space-y-2 text-xs text-gray-500 dark:text-gray-400">
                  <div className="flex items-center gap-2">
                    <Calendar className="h-3 w-3" />
                    {new Date(image.event_date).toLocaleDateString('en-US', {
                      year: 'numeric',
                      month: '2-digit',
                      day: '2-digit'
                    })}
                  </div>
                  
                  {image.event_location && (
                    <div className="flex items-center gap-2">
                      <MapPin className="h-3 w-3" />
                      {image.event_location}
                    </div>
                  )}
                  
                  {image.special_guests && (
                    <div className="flex items-center gap-2">
                      <Users className="h-3 w-3" />
                      {image.special_guests}
                    </div>
                  )}
                </div>
                
                {/* Tags */}
                <div className="flex flex-wrap gap-1 mt-3">
                  {image.tags.slice(0, 3).map(tag => (
                    <span
                      key={tag}
                      className="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded text-xs"
                    >
                      {tag}
                    </span>
                  ))}
                  {image.tags.length > 3 && (
                    <span className="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded text-xs">
                      +{image.tags.length - 3}
                    </span>
                  )}
                </div>
                
                {/* Actions */}
                <div className="flex items-center justify-between mt-4 pt-3 border-t border-gray-200 dark:border-gray-700">
                  <div className="flex items-center gap-4 text-sm text-gray-500 dark:text-gray-400">
                    <span className="flex items-center gap-1">
                      <Heart className="h-4 w-4" />
                      {image.likes}
                    </span>
                    <span className="flex items-center gap-1">
                      <MessageCircle className="h-4 w-4" />
                      {image.comments}
                    </span>
                  </div>
                  
                  <div className="flex items-center gap-2">
                    <button className="p-1 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
                      <Share2 className="h-4 w-4 text-gray-500 dark:text-gray-400" />
                    </button>
                    <button className="p-1 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
                      <Download className="h-4 w-4 text-gray-500 dark:text-gray-400" />
                    </button>
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
          </motion.div>
        )}

        {/* Empty State */}
        {!loading && !error && filteredImages.length === 0 && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-center py-16"
          >
            <Camera className="h-16 w-16 text-gray-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
              No photos found
            </h3>
            <p className="text-gray-600 dark:text-gray-300 mb-4">
              Try adjusting your search criteria or filters
            </p>
            <button
              onClick={() => {
                setSearchTerm('');
                setSelectedCategory('all');
                setSelectedTag('all');
              }}
              className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
            >
              Clear All Filters
            </button>
          </motion.div>
        )}

        {/* Lightbox Modal */}
        <AnimatePresence>
          {selectedImage && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 bg-black bg-opacity-90 z-50 flex items-center justify-center p-4"
              onClick={() => setSelectedImage(null)}
            >
              <motion.div
                initial={{ scale: 0.9, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                exit={{ scale: 0.9, opacity: 0 }}
                className="bg-white dark:bg-gray-800 rounded-lg max-w-4xl max-h-[90vh] overflow-hidden"
                onClick={(e) => e.stopPropagation()}
              >
                {/* Header */}
                <div className="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700">
                  <h2 className="text-xl font-semibold text-gray-900 dark:text-white">
                    {selectedImage.title}
                  </h2>
                  <button
                    onClick={() => setSelectedImage(null)}
                    className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full"
                  >
                    <X className="h-5 w-5" />
                  </button>
                </div>
                
                {/* Image */}
                <div className="relative">
                  <div className="w-full h-96 bg-gray-200 dark:bg-gray-700 flex items-center justify-center">
                    <Camera className="h-24 w-24 text-gray-400" />
                  </div>
                </div>
                
                {/* Details */}
                <div className="p-6">
                  <p className="text-gray-600 dark:text-gray-300 mb-4">
                    {selectedImage.description}
                  </p>
                  
                  <div className="grid md:grid-cols-2 gap-6">
                    <div>
                      <h4 className="font-semibold text-gray-900 dark:text-white mb-2">Event Details</h4>
                      <div className="space-y-2 text-sm text-gray-600 dark:text-gray-300">
                        <div className="flex items-center gap-2">
                          <Calendar className="h-4 w-4" />
                          {new Date(selectedImage.event_date).toLocaleDateString('en-US', {
                            year: 'numeric',
                            month: '2-digit',
                            day: '2-digit'
                          })}
                        </div>
                        {selectedImage.event_location && (
                          <div className="flex items-center gap-2">
                            <MapPin className="h-4 w-4" />
                            {selectedImage.event_location}
                          </div>
                        )}
                        {selectedImage.photographer && (
                          <div className="flex items-center gap-2">
                            <Camera className="h-4 w-4" />
                            Photo by {selectedImage.photographer}
                          </div>
                        )}
                      </div>
                    </div>
                    
                    <div>
                      <h4 className="font-semibold text-gray-900 dark:text-white mb-2">People & Tags</h4>
                      <div className="space-y-2 text-sm text-gray-600 dark:text-gray-300">
                        {selectedImage.people_tagged && (
                          <div>
                            <strong>People:</strong> {selectedImage.people_tagged}
                          </div>
                        )}
                        {selectedImage.special_guests && (
                          <div>
                            <strong>Special Guests:</strong> {selectedImage.special_guests}
                          </div>
                        )}
                        <div className="flex flex-wrap gap-1 mt-2">
                          {selectedImage.tags.map(tag => (
                            <span
                              key={tag}
                              className="px-2 py-1 bg-red-100 dark:bg-red-900/20 text-red-700 dark:text-red-300 rounded text-xs"
                            >
                              {tag}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  {/* Actions */}
                  <div className="flex items-center justify-between mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
                    <div className="flex items-center gap-4">
                      <button className="flex items-center gap-2 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors">
                        <Heart className="h-4 w-4" />
                        Like ({selectedImage.likes})
                      </button>
                      <button className="flex items-center gap-2 px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">
                        <MessageCircle className="h-4 w-4" />
                        Comment ({selectedImage.comments})
                      </button>
                    </div>
                    
                    <div className="flex items-center gap-2">
                      <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg">
                        <Share2 className="h-4 w-4" />
                      </button>
                      <button className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg">
                        <Download className="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
};

export default GalleryContainer;