package id.develo.capstoneproject.ui.about

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import id.develo.capstoneproject.data.local.entity.CreatorEntity
import id.develo.capstoneproject.databinding.ItemCreatorLayoutBinding

class AboutAdapter(private val listCreator: ArrayList<CreatorEntity>) :
    RecyclerView.Adapter<AboutAdapter.AboutViewHolder>() {

    inner class AboutViewHolder(private val binding: ItemCreatorLayoutBinding) :
        RecyclerView.ViewHolder(binding.root) {
        fun bind(creator: CreatorEntity) {
            with(binding) {
                tvName.text = creator.name
                tvRole.text = creator.role
                Glide.with(itemView.context)
                    .load(creator.img)
                    .into(ivCreator)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): AboutViewHolder {
        val binding =
            ItemCreatorLayoutBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return AboutViewHolder(binding)
    }

    override fun onBindViewHolder(holder: AboutViewHolder, position: Int) {
        val creator = listCreator[position]
        holder.bind(creator)
    }

    override fun getItemCount(): Int = listCreator.size
}