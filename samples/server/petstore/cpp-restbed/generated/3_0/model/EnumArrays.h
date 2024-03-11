/**
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI-Generator 7.5.0-SNAPSHOT.
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * EnumArrays.h
 *
 * 
 */

#ifndef EnumArrays_H_
#define EnumArrays_H_



#include <string>
#include <vector>
#include <memory>
#include <vector>
#include <array>
#include <boost/property_tree/ptree.hpp>
#include "helpers.h"

namespace org {
namespace openapitools {
namespace server {
namespace model {

/// <summary>
/// 
/// </summary>
class  EnumArrays 
{
public:
    EnumArrays() = default;
    explicit EnumArrays(boost::property_tree::ptree const& pt);
    virtual ~EnumArrays() = default;

    EnumArrays(const EnumArrays& other) = default; // copy constructor
    EnumArrays(EnumArrays&& other) noexcept = default; // move constructor

    EnumArrays& operator=(const EnumArrays& other) = default; // copy assignment
    EnumArrays& operator=(EnumArrays&& other) noexcept = default; // move assignment

    std::string toJsonString(bool prettyJson = false) const;
    void fromJsonString(std::string const& jsonString);
    boost::property_tree::ptree toPropertyTree() const;
    void fromPropertyTree(boost::property_tree::ptree const& pt);


    /////////////////////////////////////////////
    /// EnumArrays members

    /// <summary>
    /// 
    /// </summary>
    std::string getJustSymbol() const;
    void setJustSymbol(std::string value);

    /// <summary>
    /// 
    /// </summary>
    std::vector<std::string> getArrayEnum() const;
    void setArrayEnum(std::vector<std::string> value);

protected:
    std::string m_Just_symbol = "";
    std::vector<std::string> m_Array_enum;
};

std::vector<EnumArrays> createEnumArraysVectorFromJsonString(const std::string& json);

template<>
inline boost::property_tree::ptree toPt<EnumArrays>(const EnumArrays& val) {
    return val.toPropertyTree();
}

template<>
inline EnumArrays fromPt<EnumArrays>(const boost::property_tree::ptree& pt) {
    EnumArrays ret;
    ret.fromPropertyTree(pt);
    return ret;
}

}
}
}
}

#endif /* EnumArrays_H_ */
