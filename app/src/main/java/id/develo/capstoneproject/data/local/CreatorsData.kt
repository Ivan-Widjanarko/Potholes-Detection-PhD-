package id.develo.capstoneproject.data.local

import id.develo.capstoneproject.R
import id.develo.capstoneproject.data.local.entity.CreatorEntity

object CreatorsData {
    private val creatorNames = arrayOf(
        "Ivan Widjanarko",
        "Irfa Ramadhanti",
        "Haidar Hanif",
        "Muhammad As'ad Muyassir",
        "Muhammad Teddy Rahmansyah",
        "Faradila Alvina Putri"
    )

    private val creatorRoles = arrayOf(
        "Project Manager & Machine Learning Developer",
        "Vice Manager & Cloud Engineer",
        "Secretary & Android Developer",
        "Lead Machine Learning Developer",
        "Lead Android Developer",
        "Lead Cloud Engineer"
    )

    private val creatorImages = intArrayOf(
        R.drawable.img_ivanw,
        R.drawable.img_irfa,
        R.drawable.img_hanif,
        R.drawable.img_ads,
        R.drawable.img_teddy,
        R.drawable.img_faradila
    )

    val listData: ArrayList<CreatorEntity>
        get() {
            val list = arrayListOf<CreatorEntity>()
            for (position in creatorNames.indices) {
                val creator = CreatorEntity()
                creator.img = creatorImages[position]
                creator.name = creatorNames[position]
                creator.role = creatorRoles[position]
                list.add(creator)
            }
            return list
        }
}