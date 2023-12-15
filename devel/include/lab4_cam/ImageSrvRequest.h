// Generated by gencpp from file lab4_cam/ImageSrvRequest.msg
// DO NOT EDIT!


#ifndef LAB4_CAM_MESSAGE_IMAGESRVREQUEST_H
#define LAB4_CAM_MESSAGE_IMAGESRVREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace lab4_cam
{
template <class ContainerAllocator>
struct ImageSrvRequest_
{
  typedef ImageSrvRequest_<ContainerAllocator> Type;

  ImageSrvRequest_()
    {
    }
  ImageSrvRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ImageSrvRequest_

typedef ::lab4_cam::ImageSrvRequest_<std::allocator<void> > ImageSrvRequest;

typedef boost::shared_ptr< ::lab4_cam::ImageSrvRequest > ImageSrvRequestPtr;
typedef boost::shared_ptr< ::lab4_cam::ImageSrvRequest const> ImageSrvRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::lab4_cam::ImageSrvRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace lab4_cam

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::lab4_cam::ImageSrvRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "lab4_cam/ImageSrvRequest";
  }

  static const char* value(const ::lab4_cam::ImageSrvRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# An empty request\n"
;
  }

  static const char* value(const ::lab4_cam::ImageSrvRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ImageSrvRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::lab4_cam::ImageSrvRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::lab4_cam::ImageSrvRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // LAB4_CAM_MESSAGE_IMAGESRVREQUEST_H
